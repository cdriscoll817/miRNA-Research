              #!/usr/bin/env python
import os
import re

#ins = open( "/home/nextgen/test2.txt", "r" )

 # utr file for cow ,human,dog ....
from Bio import SeqIO
handle = open( "/home/nextgen/test2.txt", "r" ) #open("opuntia.aln", "rU rU?
for record in SeqIO.parse(handle, "fasta") :
    seq = record.seq.tostring()
    print seq
    print record.id
    seq_len = len(seq)
    seq_lens = str(seq_len)
    print seq_lens
    s.write(record.id + "\t" + seq_lens + "\n" )
s.close()
handle.close()


from biomart import BiomartServer
server = Biomatserver("http://www.biomart.org/biomart)

