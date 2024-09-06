const blocksData = [
    {
        "hash": "000000000000000000028699148bf2986da34e2e38fe8af758ea7568a2d06176",
        "height": 859686,
        "time": 1725358900,
        "block_index": 859686,
        "n_tx": 2679,
        "total_sat_val": 273790587845.0,
        "total_bitc_val": 2737.90587845
    },
    {
        "hash": "000000000000000000031595f4a0f180bcac051d208fa07edc026a6f6f9a0af8",
        "height": 859685,
        "time": 1725358680,
        "block_index": 859685,
        "n_tx": 3650,
        "total_sat_val": 1160467173744.0,
        "total_bitc_val": 11604.67173744
    }
];

const blocksContainer = document.getElementById('blocks');

// Funzione per convertire timestamp in formato leggibile
const formatTime = timestamp => {
    const date = new Date(timestamp * 1000);
    return date.toLocaleString();
};

// Ciclo per creare ogni blocco
blocksData.forEach(block => {
    const blockElement = document.createElement('div');
    blockElement.classList.add('block');

    blockElement.innerHTML = `
        <h2>Block #${block.height}</h2>
        <p><strong>Hash:</strong> ${block.hash}</p>
        <p><strong>Transactions:</strong> ${block.n_tx}</p>
        <p><strong>Time:</strong> ${formatTime(block.time)}</p>
        <p><strong>Total BTC Value:</strong> ${block.total_bitc_val} BTC</p>
    `;

    blocksContainer.appendChild(blockElement);
});
