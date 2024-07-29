#!/bin/bash

# Declaración de variable para usar la api de crossref.org para convertir un doi en un .bib para importar en zotero

declare -f doi2bib
doi2bib ()
{  
    echo >> bib.bib;
    curl -s "http://api.crossref.org/works/$1/transform//application/x-bibtex" >> bib.bib;
    echo >> bib.bib
}


