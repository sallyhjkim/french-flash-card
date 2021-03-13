<script>
  import SearchBar from "./components/SearchBar.svelte";
  import DictionaryContainer from "./components/DictionaryContainer.svelte";
  import CustombarContainer from "./components/CustombarContainer.svelte";
  import FlashCards from "./components/FlashCards.svelte";

  let flashCards = [
    { front: "a", back: "E" },
    { front: "a", back: "E" },
    { front: "a", back: "E" },
    { front: "a", back: "E" },
    { front: "a", back: "E" },
    { front: "a", back: "E" },
    { front: "a", back: "E" },
    { front: "a", back: "E" },
  ];

  const handleSearch = (e) => {
    const searchText = e.detail.search;
    // fetch here to find the dictionary items
  };

  const handleSave = (e) => {
    const opt = e.detail.option;
    let item = {
      front: opt[0].text,
      back: opt[1].text,
    };
    flashCards = flashCards.concat(item);
  };
</script>

<style>
  :global(body) {
    background-color: skyblue;
  }
  main {
    display: flex;
    flex-direction: column;
    margin: auto;
    justify-content: center;
    text-align: center;
    padding: 30px;
  }
  .searchContainer {
    margin: 10px auto;
    display: flex;
  }
  .dicinaryContainer {
    margin: 10px auto;
    display: flex;
  }
  .custombarContainer {
    margin: 10px auto;
    display: flex;
  }
  .flashCardContainer {
    margin: 10px auto;
    display: grid;
  }
</style>

<main>
  <div>
    <h1>French Flash Card🇫🇷</h1>
  </div>
  <!-- <div class="searchContainer">
    <SearchBar on:handleSearch="{handleSearch}" />
  </div> -->
  <!-- <div class="dicinaryContainer"><DictionaryContainer /></div> -->
  <div class="custombarContainer">
    <CustombarContainer on:handleSave="{handleSave}" />
  </div>
  <div class="flashCardContainer"><FlashCards flashCards="{flashCards}" /></div>
</main>
