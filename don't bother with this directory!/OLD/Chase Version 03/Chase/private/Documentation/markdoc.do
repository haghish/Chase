cd "/Users/haghish/Dropbox/Company/Projects/2016/Chase/private/Documentation"
qui log using documentation, replace
//IMPORT README.md
qui log c
markdoc documentation.smcl, exp(html)  master replace
