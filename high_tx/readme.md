# Higher tx
Focus of the program: Find the higher tx in a block by value.
Il programma è creato con 'venv' quindi per attivare l'ambiente virtuale dare il comando 'source venv/bin/activate' dentro la cartella /high_tx.

# Funzionalità del programma
Il programma mette a disposizione un endpoint flask per ricercare le n. transazioni di valore più grande all'interno di un blocco.

Indirizzo di default = http://127.0.0.1:5000/high_txs_from_block_hash
Esempio di utilizzo =  http://127.0.0.1:5000/high_txs_from_block_hash?block_hash=00000000000000000000fc7e5d1214672f23fc61b88e15617b16662af75bce98

# Come eseguire il programma
1. attivare ambiente virtuale
   - Per attivare ambiente virtuale dare il comando dentro la cartella /high_tx: 'source venv/bin/activate'
2. attivare il server
   - dare il comando: 'python3 server.py
3. utilizzare l'endpoint e attendere il risultato
   - comando di esempio:
    http://127.0.0.1:5000/high_txs_from_block_hash?block_hash=00000000000000000000fc7e5d1214672f23fc61b88e15617b16662af75bce98

    L'api restutuisce un array di oggetti di transazione in formato json. Queste sono le n. transazioni con valore più alto all'interno del blocco
4. visualizzare i dati graficamente (modificare il file index.html parte 1)
    - è possibile visualizzare i dati copiando questo oggetto json e incollandolo al posto dell'array di oggetti presende nel file index.html chiamato 'transactions'.
5. salvare il file index.html e aprirlo nel browser
6. le transazioni saranno visualizzate graficamente e ordinate per valore

## Note sul valore di una tx bitcoin
L'obiettivo di questo programma è quello di trovare la transazione più grande in un blocco bitcoin. E' necessario approfondirne il significato in quanto poco chiaro e possibile fonte di errori.

Innanzi tutto specifico che non stiamo cercando la tx che occupa più byte ma quella che contiene o sposta più valore in satoshis (1 btc = 100 000 000 satoshi).

Restando semplici è chiaro che una transazione che come input sblocca 0.2 btc è più piccola di una tx che sblocca negli input 0.8 btc. Ma è davvero così? Perchè per ipotesi possiamo pensare che la tx(1) invia 0.195 btc a un indirizzo e da 0.005 btc come fees.
La tx(2) invece invia 0.1 btc a un indirizzo, 0.005 btc come fees e come resto invia a un indirizzo 0.6995 btc.

Quindi qui abbiamo tx(1) *apparentemente* più piccola ma che in realtà trasferisce più valore ad un nuovo proprietario.
Tx(2) invece ha in apparenza un valore più grande di 0.8 btc ma nella realtà trasferisce il valore solo per 0.1 btc e i restanti 0.6995 btc rappresentano il resto.

Da questo deduco che è possibile calcolare la tx che sposta una quantità di valore maggiore ma che non è possibile nei fatti calcolare quale tx in un blocco trasfericce effettivamente il valore ad un nuovo proprietario in quanto, anche grazie all'adizione di wallet deterministici non è possibile conoscere in chiaro se un determinato output corrisponde allo stesso proprietario che ha creato la tx. Inoltre, i tx input possono appartenere a proprietari differenti facendo si che il resto possa essere distribuito verso più indirizzi rendendo il calcolo più complicato. 

Quello che penso ora è che posso fare una stima, ad es., delle 20 tx che presumibilmente spostano più valore in un blocco ma che non è possibile conoscere con precisione le tx che trasferiscono più valore a nuovi proprietari.
