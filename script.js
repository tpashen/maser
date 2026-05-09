const wheel = document.getElementById('wheel');
const totalSectors = 28;
const images = []; 

// Заповнюємо масив назвами ваших файлів (наприклад 1.png, 2.png...)
for (let i = 1; i <= totalSectors; i++) {
    images.push(`${i}.png`); 
}

// Генеруємо сектори
images.forEach((imgSrc, index) => {
    const angle = (360 / totalSectors) * index;
    const sector = document.createElement('div');
    sector.className = 'sector';
    
    // Кожен сектор повертаємо на свій кут
    sector.style.transform = `rotate(${angle}deg) translateY(-250px)`; 
    
    const img = document.createElement('img');
    img.src = imgSrc;
    img.alt = `Item ${index + 1}`;
    
    sector.appendChild(img);
    wheel.appendChild(sector);
});

// Клік для зупинки
wheel.addEventListener('click', () => {
    if (!wheel.classList.contains('stop')) {
        // Отримуємо поточний кут через getComputedStyle
        const style = window.getComputedStyle(wheel);
        const matrix = new WebKitCSSMatrix(style.transform);
        const currentAngle = Math.round(Math.atan2(matrix.b, matrix.a) * (180 / Math.PI));
        
        wheel.classList.add('stop');
        // Додаємо випадкову кількість повних обертів для ефекту казино
        const extraDegrees = 1800 + Math.floor(Math.random() * 360); 
        wheel.style.transform = `rotate(${currentAngle + extraDegrees}deg)`;
    } else {
        // Скидаємо для нового запуску
        wheel.classList.remove('stop');
        wheel.style.transform = 'none';
    }
});