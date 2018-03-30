#ifndef _SM14_H
#define _SM14_H

#define SM14_DIGEST_LENGTH	32
#define SM14_BLOCK_SIZE		64
#define SM14_CBLOCK		(SM14_BLOCK_SIZE)
#define SM14_HMAC_SIZE		(SM14_DIGEST_LENGTH)


#include <sys/types.h>
#include <stdint.h>
#include <string.h>

#ifdef __cplusplus
extern "C" {
#endif


typedef struct {
	uint32_t digest[8];
	int nblocks;
	unsigned char block[64];
	int num;
} sm14_ctx_t;

void sm14_init(sm14_ctx_t *ctx);
void sm14_update(sm14_ctx_t *ctx, const unsigned char* data, size_t data_len);
void sm14_close(void *cc, void *dst);

void sm14_final(sm14_ctx_t *ctx, unsigned char digest[sm14_DIGEST_LENGTH]);
void sm14_compress(uint32_t digest[8], const unsigned char block[sm14_BLOCK_SIZE]);
void sm14(const unsigned char *data, size_t datalen,
	unsigned char digest[sm14_DIGEST_LENGTH]);

#ifdef CPU_BIGENDIAN

#define cpu_to_be16(v) (v)
#define cpu_to_be32(v) (v)
#define be16_to_cpu(v) (v)
#define be32_to_cpu(v) (v)

#else

#define cpu_to_le16(v) (v)
#define cpu_to_le32(v) (v)
#define le16_to_cpu(v) (v)
#define le32_to_cpu(v) (v)

#define cpu_to_be16(v) (((v)<< 8) | ((v)>>8))
#define cpu_to_be32(v) (((v)>>24) | (((v)>>8)&0xff00) | (((v)<<8)&0xff0000) | ((v)<<24))
#define be16_to_cpu(v) cpu_to_be16(v)
#define be32_to_cpu(v) cpu_to_be32(v)

#endif

#ifdef __cplusplus
}
#endif
#endif
