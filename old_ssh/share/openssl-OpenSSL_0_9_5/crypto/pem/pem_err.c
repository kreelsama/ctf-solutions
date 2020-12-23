/* crypto/pem/pem_err.c */
/* ====================================================================
 * Copyright (c) 1999 The OpenSSL Project.  All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer. 
 *
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in
 *    the documentation and/or other materials provided with the
 *    distribution.
 *
 * 3. All advertising materials mentioning features or use of this
 *    software must display the following acknowledgment:
 *    "This product includes software developed by the OpenSSL Project
 *    for use in the OpenSSL Toolkit. (http://www.OpenSSL.org/)"
 *
 * 4. The names "OpenSSL Toolkit" and "OpenSSL Project" must not be used to
 *    endorse or promote products derived from this software without
 *    prior written permission. For written permission, please contact
 *    openssl-core@OpenSSL.org.
 *
 * 5. Products derived from this software may not be called "OpenSSL"
 *    nor may "OpenSSL" appear in their names without prior written
 *    permission of the OpenSSL Project.
 *
 * 6. Redistributions of any form whatsoever must retain the following
 *    acknowledgment:
 *    "This product includes software developed by the OpenSSL Project
 *    for use in the OpenSSL Toolkit (http://www.OpenSSL.org/)"
 *
 * THIS SOFTWARE IS PROVIDED BY THE OpenSSL PROJECT ``AS IS'' AND ANY
 * EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE OpenSSL PROJECT OR
 * ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 * NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
 * STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
 * OF THE POSSIBILITY OF SUCH DAMAGE.
 * ====================================================================
 *
 * This product includes cryptographic software written by Eric Young
 * (eay@cryptsoft.com).  This product includes software written by Tim
 * Hudson (tjh@cryptsoft.com).
 *
 */

/* NOTE: this file was auto generated by the mkerr.pl script: any changes
 * made to it will be overwritten when the script next updates this file.
 */

#include <stdio.h>
#include <openssl/err.h>
#include <openssl/pem.h>

/* BEGIN ERROR CODES */
#ifndef NO_ERR
static ERR_STRING_DATA PEM_str_functs[]=
	{
{ERR_PACK(0,PEM_F_D2I_PKCS8PRIVATEKEY_BIO,0),	"d2i_PKCS8PrivateKey_bio"},
{ERR_PACK(0,PEM_F_D2I_PKCS8PRIVATEKEY_FP,0),	"d2i_PKCS8PrivateKey_fp"},
{ERR_PACK(0,PEM_F_DEF_CALLBACK,0),	"DEF_CALLBACK"},
{ERR_PACK(0,PEM_F_LOAD_IV,0),	"LOAD_IV"},
{ERR_PACK(0,PEM_F_PEM_ASN1_READ,0),	"PEM_ASN1_read"},
{ERR_PACK(0,PEM_F_PEM_ASN1_READ_BIO,0),	"PEM_ASN1_read_bio"},
{ERR_PACK(0,PEM_F_PEM_ASN1_WRITE,0),	"PEM_ASN1_write"},
{ERR_PACK(0,PEM_F_PEM_ASN1_WRITE_BIO,0),	"PEM_ASN1_write_bio"},
{ERR_PACK(0,PEM_F_PEM_DO_HEADER,0),	"PEM_do_header"},
{ERR_PACK(0,PEM_F_PEM_F_DO_PK8KEY_FP,0),	"PEM_F_DO_PK8KEY_FP"},
{ERR_PACK(0,PEM_F_PEM_F_PEM_WRITE_PKCS8PRIVATEKEY,0),	"PEM_F_PEM_WRITE_PKCS8PRIVATEKEY"},
{ERR_PACK(0,PEM_F_PEM_GET_EVP_CIPHER_INFO,0),	"PEM_get_EVP_CIPHER_INFO"},
{ERR_PACK(0,PEM_F_PEM_READ,0),	"PEM_read"},
{ERR_PACK(0,PEM_F_PEM_READ_BIO,0),	"PEM_read_bio"},
{ERR_PACK(0,PEM_F_PEM_SEALFINAL,0),	"PEM_SealFinal"},
{ERR_PACK(0,PEM_F_PEM_SEALINIT,0),	"PEM_SealInit"},
{ERR_PACK(0,PEM_F_PEM_SIGNFINAL,0),	"PEM_SignFinal"},
{ERR_PACK(0,PEM_F_PEM_WRITE,0),	"PEM_write"},
{ERR_PACK(0,PEM_F_PEM_WRITE_BIO,0),	"PEM_write_bio"},
{ERR_PACK(0,PEM_F_PEM_WRITE_BIO_PKCS8PRIVATEKEY,0),	"PEM_write_bio_PKCS8PrivateKey"},
{ERR_PACK(0,PEM_F_PEM_X509_INFO_READ,0),	"PEM_X509_INFO_read"},
{ERR_PACK(0,PEM_F_PEM_X509_INFO_READ_BIO,0),	"PEM_X509_INFO_read_bio"},
{ERR_PACK(0,PEM_F_PEM_X509_INFO_WRITE_BIO,0),	"PEM_X509_INFO_write_bio"},
{0,NULL}
	};

static ERR_STRING_DATA PEM_str_reasons[]=
	{
{PEM_R_BAD_BASE64_DECODE                 ,"bad base64 decode"},
{PEM_R_BAD_DECRYPT                       ,"bad decrypt"},
{PEM_R_BAD_END_LINE                      ,"bad end line"},
{PEM_R_BAD_IV_CHARS                      ,"bad iv chars"},
{PEM_R_BAD_PASSWORD_READ                 ,"bad password read"},
{PEM_R_ERROR_CONVERTING_PRIVATE_KEY      ,"error converting private key"},
{PEM_R_NOT_DEK_INFO                      ,"not dek info"},
{PEM_R_NOT_ENCRYPTED                     ,"not encrypted"},
{PEM_R_NOT_PROC_TYPE                     ,"not proc type"},
{PEM_R_NO_START_LINE                     ,"no start line"},
{PEM_R_PROBLEMS_GETTING_PASSWORD         ,"problems getting password"},
{PEM_R_PUBLIC_KEY_NO_RSA                 ,"public key no rsa"},
{PEM_R_READ_KEY                          ,"read key"},
{PEM_R_SHORT_HEADER                      ,"short header"},
{PEM_R_UNSUPPORTED_CIPHER                ,"unsupported cipher"},
{PEM_R_UNSUPPORTED_ENCRYPTION            ,"unsupported encryption"},
{0,NULL}
	};

#endif

void ERR_load_PEM_strings(void)
	{
	static int init=1;

	if (init)
		{
		init=0;
#ifndef NO_ERR
		ERR_load_strings(ERR_LIB_PEM,PEM_str_functs);
		ERR_load_strings(ERR_LIB_PEM,PEM_str_reasons);
#endif

		}
	}
