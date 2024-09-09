# Higher tx

    - sprint 1 ---> find the higher tx in a block by value
Glossario
tx = transazione
txi = input di txssssasas

# Funzionalità del programma
Il programma permette da cercare tramite linea di comando le n. transazioni di valore più grande all'interno di un blocco.

Utilizzo:

python3 main.py get-high-tx [block_hash] [number_of_transaction_to_return]
python3 main.py get-high-tx 00000000000000000000fc7e5d1214672f23fc61b88e15617b16662af75bce98 20

The default 'number_of_transaction_to_return' is 10 and there is not a default block_hash parameter.






























## Note sul valore di una tx bitcoin
L'obiettivo di questo programma è quello di trovare la transazione più grande in un blocco bitcoin. E' necessario approfondirne il significato in quanto poco chiaro e possibile fonte di errori.

Innanzi tutto specifico che non stiamo cercando la tx che occupa più byte ma quella che contiene o sposta più valore in satoshis (1 btc = 100 000 000 satoshi).

Restando semplici è chiaro che una transazione che come input sblocca 0.2 btc è più piccola di una tx che sblocca negli input 0.8 btc. Ma è davvero così? Perchè per ipotesi possiamo pensare che la tx(1) invia 0.195 btc a un indirizzo e da 0.005 btc come fees.
La tx(2) invece invia 0.1 btc a un indirizzo, 0.005 btc come fees e come resto invia a un indirizzo 0.6995 btc.

Quindi qui abbiamo tx(1) *apparentemente* più piccola ma che in realtà trasferisce più valore ad un nuovo proprietario.
Tx(2) invece ha in apparenza un valore più grande di 0.8 btc ma nella realtà trasferisce il valore solo per 0.1 btc e i restanti 0.6995 btc rappresentano il resto.

Da questo deduco che è possibile calcolare la tx che sposta una quantità di valore maggiore ma che non è possibile nei fatti calcolare quale tx in un blocco trasfericce effettivamente il valore ad un nuovo proprietario in quanto, anche grazie all'adizione di wallet deterministici non è possibile conoscere in chiaro se un determinato output corrisponde allo stesso proprietario che ha creato la tx. Inoltre, i tx input possono appartenere a proprietari differenti facendo si che il resto possa essere distribuito verso più indirizzi rendendo il calcolo più complicato. 

Quello che penso ora è che posso fare una stima, ad es., delle 20 tx che presumibilmente spostano più valore in un blocco ma che non è possibile conoscere con precisione le tx che trasferiscono più valore a nuovi proprietari.

# Fee = Inputs - Outputs

La situazione è simile e così c'è poca precisione di calcolo ma che secondo me può essere ommessa su questo semplice esercizio perchè una commissione così bassa come quella dei bitcoin rispetto al valore delle transazioni grandi può essere trascurata.