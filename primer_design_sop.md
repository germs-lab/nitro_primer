# SOP for desinging primer using RDP's PrimerDesign



## dereplicate
```
module load USEARCH/8.0.1623
usearch -derep_fulllength fungene_9.4_amoA_AOB_437_unaligned_nucleotide_seqs.fa  -fastaout derepAOB.fasta -sizeout 

python /mnt/home/ouyangy6/Primerdesign/nifD/python/removeDup.py derepAOB.fasta derep_dup_AOB.fasta
```
## alignment
```
module load ClustalW/2.1
clustalw2 -infile=derep_dup_AOB.fasta -outfile=aligned_derep_dup_AOB.fasta -outorder=input -output=fasta
```
## taxanomy
```
python /mnt/home/ouyangy6/Primerdesign/nifD/python/getIDS.py  derep_dup_AOB.fasta > AOB_IDs
cat AOB_IDs | sed -e 's/;.*//g' > AOB_IDs_mod.txt

python /mnt/home/ouyangy6/Primerdesign/nifD/python/getLineage_by_acc.py AOB_IDs_mod.txt > AOB_tax.txt 

```



## Entropy
```
java -Xmx4g -jar /work/gunturus/netbeans/PrimerDesign/dist/PrimerDesign.jar -subcommand select -input nifD_group1_Nov2017_aligned.mfa -SlidingScale true -productLengthMin 200 -productLengthMax 300 -w anfDWeights -oligoMinSize 17 -oligoMaxSize 28 -maxMismatches 0 -tempMin 55 -tempMax 62 -hairMax 35 -homoMax 35 -isTreeWeightNeeded f -isHenikoffWeightNeeded t -os mac -output anfDPrimerswithcontrols.result -assayMax 30 -degenMax 8 -NoTEndFilter t -NoPoly3GCFilter t -PolyRunFilter 4 -GCFilterMin 0.35 -GCFilterMax 0.65 -sodiumConc 50.0 -magnesConc 1.5
```
### see the figure
```
python /work/xingziye/primers/primersplot.py Max60CoverageData.txt nifD.pdf 100 100 100
```


### primerdesign
```
java -Xmx6g -jar /work/gunturus/primer_testing/github/RDPTools/PrimerDesign/dist/PrimerDesign.jar -subcommand select -input nifD_group1_Nov2017_aligned.mfa -SlidingScale true -productLengthMin 150 -productLengthMax 300 -oligoMinSize 15 -oligoMaxSize 30 -maxMismatches 2 -tempMin 55 -tempMax 63 -hairMax 35 -homoMax 35 -isTreeWeightNeeded f -isHenikoffWeightNeeded t -os mac -output /work/ouyangy6/primerdesign/nifD/primers_nifD/nifDprimer1 -assayMax 30 -degenMax 16 -NoTEndFilter t -NoPoly3GCFilter t -PolyRunFilter 4 -GCFilterMin 0.45 -GCFilterMax 0.7 -sodiumConc 50.0 -magnesConc 1.5

java -jar /work/gunturus/primer_testing/github/RDPTools/PrimerDesign/dist/PrimerDesign.jar -subcommand select -input nifD_group1_Nov2017_aligned.mfa -SlidingScale true -productLengthMin 150 -productLengthMax 300 -oligoMinSize 15 -oligoMaxSize 30 -maxMismatches 2 -tempMin 55 -tempMax 63 -hairMax 35 -homoMax 35 -isTreeWeightNeeded f -isHenikoffWeightNeeded t -os mac -output /work/leotift/CmdLineResults -assayMax 30 -degenMax 16 -NoTEndFilter t -NoPoly3GCFilter t -PolyRunFilter 4 -GCFilterMin 0.45 -GCFilterMax 0.7 -sodiumConc 50.0 -magnesConc 1.5

java -jar /work/gunturus/primer_testing/github/RDPTools/PrimerDesign/dist/PrimerDesign.jar -subcommand select -input nifD_group1_Nov2017_aligned.mfa -SlidingScale false -forwardMinPos 450 -forwardMaxPos 550 - reverseMinPos 710 -reverseMaxPos 780 -oligoMinSize 15 -oligoMaxSize 30 -maxMismatches 2 -tempMin 55 -tempMax 63 -hairMax 35 -homoMax 35 -isTreeWeightNeeded f -isHenikoffWeightNeeded t -os mac -output /work/ouyangy6/primerdesign/nifD/primers_nifD/nifDprimer2 -assayMax 30 -degenMax 6 -NoTEndFilter t -NoPoly3GCFilter t -PolyRunFilter 4 -GCFilterMin 0.45 -GCFilterMax 0.7 -sodiumConc 50.0 -magnesConc 1.5
```
### HPCC
```
module load Java/jdk1.8.0
java -jar /mnt/research/rdp/public/github/RDPTools/PrimerDesign/dist/PrimerDesign.jar -subcommand select -input nifD_group1_Nov2017_aligned.mfa -SlidingScale true -productLengthMin 150 -productLengthMax 300 -oligoMinSize 15 -oligoMaxSize 30 -maxMismatches 2 -tempMin 55 -tempMax 63 -hairMax 35 -homoMax 35 -isTreeWeightNeeded f -isHenikoffWeightNeeded t -os mac -output nifDprimer_slidingScale -assayMax 30 -degenMax 16 -NoTEndFilter t -NoPoly3GCFilter t -PolyRunFilter 4 -GCFilterMin 0.45 -GCFilterMax 0.7 -sodiumConc 50.0 -magnesConc 1.5

module load Java/jdk1.8.0
java -jar /mnt/research/rdp/public/github/RDPTools/PrimerDesign/dist/PrimerDesign.jar -subcommand select -input nifD_group1_Nov2017_aligned.mfa -SlidingScale false -forwardMinPos 450 -forwardMaxPos 550 -reverseMinPos 710 -reverseMaxPos 780 -oligoMinSize 15 -oligoMaxSize 30 -maxMismatches 2 -tempMin 55 -tempMax 63 -hairMax 35 -homoMax 35 -isTreeWeightNeeded f -isHenikoffWeightNeeded t -os mac -output nifDprimer_450_780 -assayMax 30 -degenMax 6 -NoTEndFilter t -NoPoly3GCFilter t -PolyRunFilter 4 -GCFilterMin 0.45 -GCFilterMax 0.7 -sodiumConc 50.0 -magnesConc 1.5
```
