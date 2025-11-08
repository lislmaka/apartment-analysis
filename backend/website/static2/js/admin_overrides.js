document.addEventListener("DOMContentLoaded", function () {

    const showFiltersLink = document.createElement("a");
    showFiltersLink.href = "#";
    showFiltersLink.textContent = "←  Развернуть фильтры";
    const showFiltersDiv = document.createElement("div");
    showFiltersDiv.id = "show-filters";
    showFiltersDiv.style.float = "right";
    showFiltersDiv.appendChild(showFiltersLink);
    const actionsDiv = document.querySelector("div.actions");
    actionsDiv.insertBefore(showFiltersDiv, actionsDiv.firstChild);
    // showFiltersDiv.style.display = "block";

    const changelistFilter = document.querySelector("#changelist-filter");
    changelistFilter.style.display = "none";
    showFiltersDiv.style.display = "block";

    const hideFiltersLink = document.createElement("a");
    hideFiltersLink.href = "#";
    hideFiltersLink.style.color = "white";
    hideFiltersLink.id = "hide-filters";
    hideFiltersLink.textContent = "Свернуть фильтры →";
    const changelistFilterH2 = document.querySelector("#changelist-filter h2");
    changelistFilterH2.innerHTML = "";
    changelistFilterH2.appendChild(hideFiltersLink);

    showFiltersLink.addEventListener("click", function () {
        const changelistFilter = document.querySelector("#changelist-filter");
        changelistFilter.style.display = "block";
        const changelist = document.querySelector("#changelist");
        changelist.classList.add("filtered");
        showFiltersDiv.style.display = "none";
    });

    hideFiltersLink.addEventListener("click", function () {
        const changelistFilter = document.querySelector("#changelist-filter");
        changelistFilter.style.display = "none";
        showFiltersDiv.style.display = "block";
        const changelist = document.querySelector("#changelist");
        changelist.classList.remove("filtered");
    });
  
});