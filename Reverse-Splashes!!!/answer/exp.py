with open('splashes.txt', 'r') as f:
    for l in f.readlines():
        if '§' in l:
            print(l.strip())

# Cipher: yzvk{djrwvkoax_pzhk_lh_kcc_epx_lkr_hcmj_wijlbci}
# Key: toverbest