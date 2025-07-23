// Noticias tipo ticker inferior
document.addEventListener('DOMContentLoaded', () => {
    const headlines = [
        "⚽ Real Madrid gana la Supercopa en penales",
        "🏀 Steph Curry anota 45 puntos frente a Lakers",
        "🏈 Mahomes lanza 4 TDs y lidera victoria de Chiefs",
        "🎾 Alcaraz avanza a semifinales del US Open",
        "🏆 Messi marca doblete en final de Copa Intercontinental"
    ];

    let index = 0;
    const ticker = document.createElement('div');
    ticker.style.position = 'fixed';
    ticker.style.bottom = '0';
    ticker.style.left = '0';
    ticker.style.width = '100%';
    ticker.style.background = '#c8102e';
    ticker.style.color = 'white';
    ticker.style.padding = '10px';
    ticker.style.fontWeight = 'bold';
    ticker.style.fontSize = '16px';
    ticker.style.textAlign = 'center';
    ticker.style.zIndex = '9999';
    ticker.innerText = headlines[index];
    document.body.appendChild(ticker);

    setInterval(() => {
        index = (index + 1) % headlines.length;
        ticker.innerText = headlines[index];
    }, 4000);
});
