#!/bin/bash

directory="./Masq" 
if [[ -d $directory ]] 
then
mv *_MasqPlan.tif ./Masq/
else
mkdir Masq && mv *_MasqPlan.tif ./Masq/
fi

