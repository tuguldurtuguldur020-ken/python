
"use strict";

// 1. HTML элементүүдээ сонгоно
const menuToggle = document.getElementById("menuToggle");
const navLinks = document.getElementById("navLinks");

const searchInput = document.getElementById("searchInput");
const gameCards = document.querySelectorAll(".game-card");
const emptyMessage = document.getElementById("emptyMessage");

const detailButtons = document.querySelectorAll(".details-btn");

// 2. Гар утасны menu нээж, хаах
menuToggle.addEventListener("click", function () {
    navLinks.classList.toggle("active");
});

// Menu дээрх холбоос дарахад menu хаагдана
navLinks.querySelectorAll("a").forEach(function (link) {
    link.addEventListener("click", function () {
        navLinks.classList.remove("active");
    });
});

// 3. Тоглоом хайх
searchInput.addEventListener("input", function () {
    const searchText = searchInput.value.toLowerCase().trim();

    let visibleCount = 0;

    gameCards.forEach(function (card) {
        const gameName = card.dataset.name.toLowerCase();

        if (gameName.includes(searchText)) {
            card.style.display = "";
            visibleCount++;
        } else {
            card.style.display = "none";
        }
    });

    // Хайлтаар тоглоом олдоогүй үед мессеж харуулна
    if (visibleCount === 0) {
        emptyMessage.style.display = "block";
    } else {
        emptyMessage.style.display = "none";
    }
});

// 4. Тоглоомын мэдээлэл харуулах
detailButtons.forEach(function (button) {
    button.addEventListener("click", function () {
        const gameName = button.dataset.game;

        alert(
            "Тоглоом: " + gameName +
            "\n\nТа " + gameName +
            " тоглоомыг сонголоо!"
        );
    });
});

// 5. Console дээр ажиллаж байгааг шалгах
console.log("NEXUS GAMING website loaded!");
