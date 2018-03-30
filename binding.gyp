{
    "targets": [
        {
            "target_name": "multihashing",
            "sources": [
                "sha3/sph_haval.c",
                "sha3/sph_ripemd.c",
                "sha3/sph_sha2.c",
                "sha3/sph_sha2big.c",
                "sha3/sph_tiger.c",
                "multihashing.cc",
                "scryptjane.c",
                "scryptn.c",
                "keccak.c",
                "skein.c",
                "x11.c",
                "quark.c",
                "bcrypt.c",
                "groestl.c",
                "blake.c",
                "gost.c",
                "fugue.c",
                "qubit.c",
                "hefty1.c",
                "shavite3.c",
                "cryptonight.c",
                "x13.c",
		"x13bcd.c",
                "boolberry.cc",
                "nist5.c",
                "whirlpoolx.c",
                "Lyra2RE.c",
                "zr5.c",
                "Lyra2.c",
                "Sponge.c",
                "Lyra2REV2.c",
		"Lyra2Z.c",
                "blake2s.c",
                "sha3/sph_blake2s.c",
                "neoscrypt.c",
                "sha1.c",
                "x15.c",
                "fresh.c",
                "phi1612.c",
                "sph/sph_skein.h",
                "sph/sph_jh.h",  
                "sph/sph_cubehash.h", 
                "sph/sph_fungue.h",
                "sph/sph_gost.h",
                "sph/sph_echo.h",
		"sm14.c",
                "hsr14.c",
                "tribus.c",
                "yescrypt/sha256_Y.c",
                "yescrypt/yescrypt-best.c",
                "yescrypt/yescryptcommon.c",
                "sha3/sph_hefty1.c",
                "sha3/aes_helper.c",
                "sha3/sph_blake.c",
                "sha3/sph_bmw.c",
                "sha3/sph_cubehash.c",
                "sha3/sph_echo.c",
                "sha3/sph_groestl.c",
                "sha3/sph_gost.c",
                "sha3/sph_jh.c",
                "sha3/sph_keccak.c",
                "sha3/sph_luffa.c",
                "sha3/sph_shavite.c",
                "sha3/sph_simd.c",
                "sha3/sph_skein.c",
                "sha3/sph_whirlpool.c",
                "sha3/sph_shabal.c",
                "sha3/hamsi.c", 
		"sha3/sm3.c",
                "magimath.c",
                "m7.c",
                "crypto/oaes_lib.c",
                "crypto/c_keccak.c",
                "crypto/c_groestl.c",
                "crypto/c_blake256.c",
                "crypto/c_jh.c",
                "crypto/c_skein.c",
                "crypto/hash.c",
                "crypto/aesb.c",
                "crypto/wild_keccak.cpp",
                "sha3/sph_fugue.c",
                "lyra2z16m330.c",
                "skunk.c",
                "lyra2z330.c",
                "xevan.c"
            ],
            'conditions': [
                ['OS=="linux"',
                  {
                    'link_settings': {
                      'libraries': [
                        '-lgmp'
                      ]
                    }
                  }
                ],
                ['OS=="mac"',
                  {
                    'link_settings': {
                      'libraries': [
                        '-lgmp'
                      ]
                    }
                  }
                ],
                ['OS=="win"',
                  {
                    'link_settings': {
                      'libraries': [
                        '-lgmp.lib'
                      ],
                    }
                  }
                ]
              ],
            "include_dirs": [
                "crypto",
                "<!(node -e \"require('nan')\")"
            ],
            "cflags_cc": [
                "-std=c++0x"
            ],
        }
    ]
}
