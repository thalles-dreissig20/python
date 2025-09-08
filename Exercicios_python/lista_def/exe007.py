def pode_passar(A, B, C, H, L):
    return (
        (A <= H and B <= L) or (A <= L and B <= H) or
        (A <= H and C <= L) or (A <= L and C <= H) or
        (B <= H and C <= L) or (B <= L and C <= H) or
        (B <= H and A <= L) or (B <= L and A <= H) or
        (C <= H and A <= L) or (C <= L and A <= H) or
        (C <= H and B <= L) or (C <= L and B <= H)
    )

A, B, C = map(int, input().split())
H, L = map(int, input().split())

if pode_passar(A, B, C, H, L):
    print('S')
else:
    print('N')