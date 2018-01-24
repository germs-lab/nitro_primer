# SOP for blast environmental sample into targeted gene database


## Download environmental metagenome file
### MG-RAST
```
git clone https://github.com/metajinomics/mg_rast_tools.git
```
#### get metadata using search
using conda in HPC
```
source /mnt/research/germs/softwares/anaconda2/bin/activate conda
```
now get meta table
```
cd mg_rast_tools
python get_meta_from_search.py --meta_field mgrast_field.txt --outfile soil.meta.tsv --sequence_type wgs --material soil
```
#### get command to download
```
for x in *.tsv;
do python get_command_mgrast_from_searchresultmetadata.py $x > $x.command.mgrast.download.sh;
done
```

copy command to upper directory
```
cp *.command.mgrast.download.sh ../
```

now, run. Generate qsub file then run
```
cat command.mgrast.download.sh | parallel
```


### SRA
```
add command
```

## Convert fastq into fasta
```
for x in *.fastq;do echo "cat $x | paste - - - - | sed 's/^@/>/g'| cut -f1-2 | tr '\t' '\n' > ${x%.fastq*}.fna";done > command.diamond.sh
cat command.diamond.sh | parallel
```

## Diamond
### Old version v0.7.9.58
make database
```
module load diamond
diamond makedb --in nifH.faa -d nifH.database
```
then run
```
mkdir temp
for x in *.fastq;
do echo "diamond blastx -d narG.database.dmnd -q $x -a $x -t temp";
done > command.fastq.diamond.sh
cat command.fastq.diamond.sh | parallel

for x in *.fna;
do echo "diamond blastx -d narG.database.dmnd -q $x -a $x -t temp";
done > command.fna.diamond.sh
cat command.fna.diamond.sh | parallel

for x in *.daa;
do echo "diamond view -a $x -o $x.m8";
done> command.view.diamond.sh
cat command.view.diamond.sh | parallel

```
### this is for new version v0.9.14
make database
```
/mnt/research/germs/softwares/diamond-0.9.14/bin/diamond makedb --in narG_clustered_95.fa -d narG.databse.0.9.14
```
run

```
for x in *.fastq;
do echo "/mnt/research/germs/softwares/diamond-0.9.14/bin/diamond blastx -d narG.databse.0.9.14 -q $x -o $x.m8";
done > command.fastq.diamond.sh
cat command.fastq.diamond.sh | parallel

for x in *.fna;
do echo "/mnt/research/germs/softwares/diamond-0.9.14/bin/diamond blastx -d narG.databse.0.9.14 -q $x -o $x.m8";
done > command.fna.diamond.sh
cat command.fna.diamond.sh | parallel

```


## filter result of diamond
```
make_count_diamond.py *.m8 > count.txt
```
