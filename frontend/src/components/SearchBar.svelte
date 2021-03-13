<script>
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();

  const handleSearch = (e) => {
    if (e.keyCode !== 13) return;
    const val = e.target.value;
    dispatch("handleSearch", { search: val });
  };

  const handleSearchClick = (e) => {
    const searchText = document.querySelector("#searchInput");
    dispatch("handleSearch", { search: searchText.value });
  };
</script>

<style></style>

<div>
  <input id="searchInput" type="text" on:keydown="{handleSearch}" />
  <button id="searchButton" on:click="{handleSearchClick}">search</button>
  <button>eye</button>
</div>
