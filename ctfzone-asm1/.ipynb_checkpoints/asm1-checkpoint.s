	.file	"asm1.c"
	.intel_syntax noprefix
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	push	rbp
	.cfi_def_cfa_offset 16  # CFA offset to 16
	.cfi_offset 6, -16      # save 6 at CFA[-16]
	mov	rbp, rsp
	.cfi_def_cfa_register 6 # CFA set to 6
	push	r12
	push	rbx
	.cfi_offset 12, -24
	.cfi_offset 3, -32
	mov	r12d, 0
	mov	ebx, 0
	jmp	.L2
.L3:
	add	r12d, ebx
	add	ebx, 2
.L2:
	cmp	ebx, 2017
	jbe	.L3# if ebx < 1027
	mov	eax, r12d
	pop	rbx
	pop	r12
	pop	rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.10) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
