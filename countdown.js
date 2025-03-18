function countdown(seconds) {
    let interval = setInterval(() => {
        if (seconds > 0) {
            console.log(`⏳ ${seconds} seconds remaining...`);
            seconds--;
        } else {
            console.log("🚀 Time's up!");
            clearInterval(interval);
        }
    }, 1000);
}

countdown(10); // Change the number to set a different countdown
