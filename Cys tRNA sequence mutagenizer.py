trna5 = 'GGCGCGTTAACAAAGCGGTTATGTAGCGGATT'
trna3 = 'AATCCGTCTAGTCCGGTTCGACTCCGGAACGCGCCTCCA'
trnaAC_R = 'tcg'
trnaAC_D = 'gtc'
flank5 = 'cccctctaga'
flank3 = 'tgggaaagataag'

mut_trna5 = trna5.replace('G','(02029402)').replace('C','(02940202)').replace('T','(02020294)').replace('A','(94020202)')
mut_trna3 = trna3.replace('G','(02029402)').replace('C','(02940202)').replace('T','(02020294)').replace('A','(94020202)')

mut_trna_R = flank5+trna5+trnaAC_R+trna3+flank3
mut_trna_D = flank5+trna5+trnaAC_D+trna3+flank3

print 'R:\n', mut_trna_R
print 'D:\n', mut_trna_D