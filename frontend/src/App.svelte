<script>
  import SearchBar from "./components/SearchBar.svelte";
  import DictionaryContainer from "./components/DictionaryContainer.svelte";
  import CustombarContainer from "./components/CustombarContainer.svelte";
  import FlashCards from "./components/FlashCards.svelte";

  const ENDPOINT = "http://localhost:8000/api/flashcards/";
  let flashCards = [];
  fetch(ENDPOINT)
    .then((response) => response.json())
    .then((data) => {
      flashCards = [...data];
    });

  const handleSearch = (e) => {
    const searchText = e.detail.search;
    // fetch here to find the dictionary items
  };

  const handleSave = (e) => {
    const opt = e.detail.option;
    let data = {
      new_flashcard: {
        french: opt[0].text,
        english: opt[1].text,
        description: null,
      },
    };
    fetch(ENDPOINT, {
      method: "POST",
      body: JSON.stringify(data),
    })
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        console.log("data", data);
        flashCards.push(data);
        flashCards = [...flashCards];
      });
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
