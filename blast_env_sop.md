# SOP for blast environmental sample into targeted gene database


## Download environmental metagenome file
### MG-RAST
```
git clone https://github.com/metajinomics/mg_rast_tools.git
```
#### get metadata using search
```
python get_meta_from_search.py --meta_field mgrast_field.txt --outfile soil.meta.tsv --sequence_type wgs --material soil
```
#### get command to download
```
python get_command_mgrast_from_searchresultmetadata.py soil.meta.tsv > command.mgrast.download.sh
cat command.mgrast.download.sh | parallel
```


### SRA
```
add command
```

## Convert fastq into fasta
```
for x in *.fastq;do echo "cat $x | paste - - - - | sed 's/^@/>/g'| cut -f1-2 | tr '\t' '\n' > ${x%.fastq*}.fasta";done > command.diamond.sh
cat command.diamond.sh | parallel
```

## Diamond
```
diamond makedb --in nifH.faa -d nifH.database
for x in *.fasta;
do echo "diamond blastx -d nifH.database -q $x -o $x.matcheds.m8" > command.diamond.sh;
done
cat command.diamond.sh | parallel
```


## filter result of diamond
```
add command
```
