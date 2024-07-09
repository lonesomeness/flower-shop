document.addEventListener('DOMContentLoaded', () => {
  let shop = document.getElementById("shop");
  let basket = JSON.parse(localStorage.getItem("data")) || [];

  let generateShop = () => {
      shop.innerHTML = productsData.map((product) => {
          let { id, name, price, description, image_url } = product;
          let search = basket.find((item) => item.id === id) || { item: 0 };
          return `
              <div id="product-id-${id}" class="item">
                  <img width="220" src="${image_url}" alt="${name}">
                  <div class="details">
                      <h3>${name}</h3>
                      <p>${description}</p>
                      <div class="price-quantity">
                          <h2>${price} ₽</h2>
                          <div class="buttons">
                              <i onclick="decrement(${id})" class="bi bi-dash-lg"></i>
                              <div id="${id}" class="quantity">${search.item}</div>
                              <i onclick="increment(${id})" class="bi bi-plus-lg"></i>
                          </div>
                      </div>
                  </div>
              </div>
          `;
      }).join("");
  };

  generateShop();

  let increment = (id) => {
      let selectedItem = productsData.find((product) => product.id === id);
      let search = basket.find((item) => item.id === id);

      if (search === undefined) {
          basket.push({
              id: selectedItem.id,
              item: 1,
          });
      } else {
          search.item += 1;
      }

      update(id);
      localStorage.setItem("data", JSON.stringify(basket));
  };

  let decrement = (id) => {
      let selectedItem = productsData.find((product) => product.id === id);
      let search = basket.find((item) => item.id === id);

      if (search === undefined || search.item === 0) return;

      search.item -= 1;
      update(id);
      basket = basket.filter((item) => item.item !== 0);
      localStorage.setItem("data", JSON.stringify(basket));
  };

  let update = (id) => {
      let search = basket.find((item) => item.id === id);
      document.getElementById(id).textContent = search.item;
      calculation();
  };

  let calculation = () => {
      let cartAmount = basket.reduce((total, item) => total + item.item, 0);
      document.getElementById("cartAmount").textContent = cartAmount;
  };

  calculation();
});
