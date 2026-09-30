"""Independent re-check of the shortest-side skeleton theorem.

Deliberately NOT sharing code with the paper's ancillary scripts: cells are handled in
CUBE coordinates (x, y, z) with x+y+z = 0, adjacency = differ by a permutation of
(+1,-1,0), and the six extreme lines are read off as min/max of x, y, z.
"""
import math, itertools

def isqrt_ceil(v):
    r = math.isqrt(v)
    return r if r * r == v else r + 1

def g(N):   return isqrt_ceil(12 * N - 3)
def M(t):   return (t * t + 3) // 12 if t >= 0 else 0

NB = [(1,-1,0),(-1,1,0),(0,1,-1),(0,-1,1),(1,0,-1),(-1,0,1)]
def nbrs(c):
    x,y,z = c; return [(x+a,y+b,z+d) for a,b,d in NB]
def perim(S):
    return sum(1 for c in S for n in nbrs(c) if n not in S)
def conn(S):
    st=[next(iter(S))]; seen=set(st)
    while st:
        c=st.pop()
        for n in nbrs(c):
            if n in S and n not in seen: seen.add(n); st.append(n)
    return len(seen)==len(S)
def lines(S):
    return {(0,c[0]) for c in S}|{(1,c[1]) for c in S}|{(2,c[2]) for c in S}
def runs(S):
    R=0
    for ax,k in lines(S):
        o=(ax+1)%3
        vals=sorted(c[o] for c in S if c[ax]==k)
        R+=1+sum(1 for i in range(len(vals)-1) if vals[i+1]-vals[i]>1)
    return R
def dconv(S): return runs(S)==len(lines(S))
def canon(S):
    m=[min(c[i] for c in S) for i in range(3)]
    # translate so that min x = min y = 0 (then z is determined)
    dx,dy=m[0],m[1]
    return frozenset((c[0]-dx,c[1]-dy,c[2]+dx+dy) for c in S)
def extreme_lines(S):
    out=[]
    for ax in range(3):
        vals=[c[ax] for c in S]
        for k in (min(vals),max(vals)):
            out.append(frozenset(c for c in S if c[ax]==k))
    return out

# --- enumerate minimizers via regular growth up to N=13, then via "hexagonal hull" subsets
def grow(fam):
    out=set()
    for S in fam:
        for c in S:
            for n in nbrs(c):
                if n not in S: out.add(canon(S|{n}))
    return out

def hull_cells(S):
    lo=[min(c[i] for c in S) for i in range(3)]; hi=[max(c[i] for c in S) for i in range(3)]
    cells=set()
    for x in range(lo[0],hi[0]+1):
        for y in range(lo[1],hi[1]+1):
            z=-x-y
            if lo[2]<=z<=hi[2]: cells.add((x,y,z))
    return cells

def minimizers_by_hull(N, slack=4):
    """All N-cell minimizers: hulls with lambda = g(N), remove <= slack cells."""
    ga=g(N); out=set()
    # enumerate hexagonal hulls by their three ranges; lambda = sum of ranges
    for wx in range(1,ga):
        for wy in range(1,ga-wx):
            wz=ga-wx-wy
            if wz<1: continue
            # hull = {x in [0,wx-1], y in [0,wy-1], z=-x-y in [zlo, zlo+wz-1]}
            for zlo in range(-(wx-1)-(wy-1), 1):
                H={(x,y,-x-y) for x in range(wx) for y in range(wy) if zlo<=-x-y<=zlo+wz-1}
                if not H or len(lines(H))!=ga: continue
                d=len(H)-N
                if d<0 or d>slack: continue
                for rem in itertools.combinations(sorted(H),d):
                    S=H-set(rem)
                    if conn(S) and perim(S)==2*ga: out.add(canon(S))
    return out

def restore_order(S, row, Sp):
    """Lemma 4.1(ii): start from a cell of row adjacent to Sp, extend along the row."""
    row=sorted(row); 
    ax=[i for i in range(3) if len({c[i] for c in row})==1][0]; o=(ax+1)%3
    row.sort(key=lambda c:c[o])
    anchor=[i for i,c in enumerate(row) if any(n in Sp for n in nbrs(c))]
    if not anchor: return None
    i=anchor[0]; order=[row[i]]; l,r=i-1,i+1
    while l>=0 or r<len(row):
        if r<len(row): order.append(row[r]); r+=1
        if l>=0: order.append(row[l]); l-=1
    return order

def main():
    tot=fail=fail_restore=0; ns_tot=ns_min=0
    for N in range(3,35):
        for S in minimizers_by_hull(N):
            S=set(S); sg=perim(S)//2
            assert sg==g(N) and dconv(S)
            ext=extreme_lines(S); rho=min(len(e) for e in ext)
            for e in ext:
                Sp=S-e
                if not Sp: continue
                if len(e)==rho:
                    tot+=1
                    ok=conn(Sp) and dconv(Sp) and perim(Sp)==2*g(len(Sp)) and g(len(Sp))==sg-1
                    if not ok: fail+=1; continue
                    order=restore_order(S,e,Sp)
                    if order is None: fail_restore+=1; continue
                    T=set(Sp)
                    for c in order:
                        T.add(c)
                        if not(conn(T) and dconv(T) and perim(T)-2*g(len(T))<=2): fail_restore+=1; break
                else:
                    ns_tot+=1
                    if conn(Sp) and perim(Sp)==2*g(len(Sp)): ns_min+=1
    print(f"shortest-line peelings of minimizers, 3<=N<=34: {tot}")
    print(f"  not a minimizer with g down by 1: {fail}")
    print(f"  restoration order violating exc<=2 / convexity / connectedness: {fail_restore}")
    print(f"non-shortest peelings: {ns_tot}, landing on a minimizer: {ns_min}")
    # residue table
    bad=0
    for s_ in range(6,3000):
        m,s=divmod(s_,6)
        d=M(s_-1)-M(s_-2); L=(s_+3)//6
        if d!=(m+1 if s==4 else m) or L!=(m if s<=2 else m+1): bad+=1
    print("residue table sigma<=2999 mismatches:",bad)
    Nb=lambda ga:min(N for N in range(1,20000) if g(N)==ga)
    assert all(Nb(6*m+3)==M(6*m+2)+1==3*m*m+2*m+1 and Nb(6*m+5)==M(6*m+4)+1==3*m*m+4*m+2 for m in range(1,60))
    print("N_b = M(sigma-1)+1 and boundary counts 3m^2+2m+1, 3m^2+4m+2 for m<=59: OK")

if __name__=='__main__':
    main()
