#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include "meow_hash_x64_aesni.h"

using namespace std;

#define movdqu(A, B)	    A = _mm_loadu_si128((__m128i *)(B))
#define movq(A, B)          A = _mm_set_epi64x(0, B);
#define aesenc(A, B)	    A = _mm_aesenc_si128(A, B)
#define pshufb(A, B)        A = _mm_shuffle_epi8(A, B)
#define pxor(A, B)	        A = _mm_xor_si128(A, B)
#define psubq(A, B)	        A = _mm_sub_epi64(A, B)
#define pand(A, B)          A = _mm_and_si128(A, B)
#define palignr(A, B, i)    A = _mm_alignr_epi8(A, B, i)
#define pxor_clear(A, B)	A = _mm_setzero_si128(); 

#define INSTRUCTION_REORDER_BARRIER _ReadWriteBarrier()
#define MEOW_INV_MIX_REG(r1, r2, r3, r4, r5,  i1, i2, i3, i4) \
pxor(r4, i4);                \
psubq(r5, i3);               \
aesenc(r2, r4);              \
INSTRUCTION_REORDER_BARRIER; \
pxor(r2, i2);                \
psubq(r3, i1);               \
aesenc(r1, r2);              \
INSTRUCTION_REORDER_BARRIER;

#define MEOW_INV_SHUFFLE(r0, r1, r2, r4, r5, r6) \
pxor(r1, r2);     \
aesenc(r4, r1);   \
psubq(r5, r6);    \
pxor(r4, r6);     \
psubq(r1, r5);    \
aesenc(r0, r4);

static void PrintHash(meow_u128 Hash) {
    printf("    %08X-%08X-%08X-%08X\n",
        MeowU32From(Hash, 3),
        MeowU32From(Hash, 2),
        MeowU32From(Hash, 1),
        MeowU32From(Hash, 0));
}

static void PrintKey(meow_u128 Hash1, meow_u128 Hash2)
{
    printf("\t%08X%08X%08X%08X%08X%08X%08X%08X\n",
        MeowU32From(Hash1, 3),
        MeowU32From(Hash1, 2),
        MeowU32From(Hash1, 1),
        MeowU32From(Hash1, 0),
        MeowU32From(Hash2, 3),
        MeowU32From(Hash2, 2),
        MeowU32From(Hash2, 1),
        MeowU32From(Hash2, 0));
}

meow_u8 Key[128] =
{
    0xCA, 0x2C, 0xC5, 0x05, 0x43, 0xFD, 0xA1, 0x3E,
    0x9D, 0x76, 0x28, 0x0A, 0x3B, 0x51, 0x72, 0x22,
    0x4C, 0x07, 0x75, 0x89, 0xB1, 0x4D, 0x4D, 0x1D,
    0x88, 0x4E, 0x18, 0xC3, 0xD9, 0xFE, 0xD8, 0xA0,
    0xA7, 0x74, 0xDA, 0x6D, 0x79, 0xC9, 0xC2, 0xF9,
    0xD5, 0x2E, 0xC2, 0x11, 0x0A, 0x47, 0xF6, 0x98,
    0xB3, 0x9F, 0xBA, 0x4C, 0x8E, 0x6A, 0xCD, 0x14,
    0x5C, 0x2A, 0xA6, 0xC3, 0x4F, 0x51, 0x93, 0xED,
    0x3F, 0x65, 0xD9, 0xE7, 0x5B, 0x58, 0x69, 0x37,
    0x2D, 0xC1, 0x56, 0xCA, 0xB7, 0x41, 0x24, 0x89,
    0xB1, 0x42, 0x3E, 0x55, 0xF8, 0xC6, 0xC0, 0x85,
    0x83, 0xB0, 0x3E, 0xFF, 0x05, 0x8D, 0x21, 0xCC,
    0x6F, 0x12, 0x84, 0xE9, 0xC0, 0x05, 0x73, 0x33,
    0x30, 0xC3, 0x58, 0x3E, 0xEF, 0x48, 0x15, 0xDF,
    0xB7, 0x9C, 0xE0, 0x90, 0xE2, 0x4A, 0xDE, 0x5B,
    0xA5, 0xD0, 0xB5, 0x67, 0x5A, 0xF4, 0x4F, 0x92
};

static void Invertibility(meow_umm Len)
{
    meow_u128 xmm0, xmm1, xmm2, xmm3, xmm4, xmm5, xmm6, xmm7;
    meow_u128 xmm8, xmm9, xmm10, xmm11, xmm12, xmm13, xmm14, xmm15;

    pxor_clear(xmm0);
    pxor_clear(xmm1);
    pxor_clear(xmm2);
    pxor_clear(xmm3);
    pxor_clear(xmm4);
    pxor_clear(xmm5);
    pxor_clear(xmm6);
    pxor_clear(xmm7);

    pxor_clear(xmm9, xmm9);
    pxor_clear(xmm11, xmm11);

    xmm8 = xmm9;
    xmm10 = xmm9;
    palignr(xmm8, xmm11, 15);
    palignr(xmm10, xmm11, 1);

    pxor_clear(xmm12, xmm12);
    pxor_clear(xmm13, xmm13);
    pxor_clear(xmm14, xmm14);
    movq(xmm15, Len);
    palignr(xmm12, xmm15, 15);
    palignr(xmm14, xmm15, 1);
    MEOW_INV_MIX_REG(xmm1, xmm5, xmm7, xmm2, xmm3, xmm12, xmm13, xmm14, xmm15);
    MEOW_INV_MIX_REG(xmm0, xmm4, xmm6, xmm1, xmm2, xmm8, xmm9, xmm10, xmm11);
    printf("%s\n", "Key: ");
    PrintHash(xmm0);
    PrintHash(xmm1);
    PrintHash(xmm2);
    PrintHash(xmm3);
    PrintHash(xmm4);
    PrintHash(xmm5);
    PrintHash(xmm6);
    PrintHash(xmm7);
    return;
}
int main()
{
    const char* Message = "sducstiaepsducstiaepsducstiaepsducstiaepsducstiaepsducstiaepsduc";
    const int Len = strlen(Message);
	char* message = new char[Len + 1];
	memset(message, 0, Len + 1);
	memcpy(message, Message, Len);
	cout << "Message: " << Message << "  Length:" << Len << endl;
	Invertibility(Len);
	meow_u128 Hash = MeowHash(Key, Len, message);
	cout << "Hashed Message:" << endl;
	PrintHash(Hash);
	delete[] Message;
	return 0;
}
