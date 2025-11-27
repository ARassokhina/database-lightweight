<template>
  <div id="app">
    <table>
      <caption>
        Таблица расхода материала за 2025 год
      </caption>
      <thead>
        <tr>
          <th :key="header.display" v-for="header in headers">{{ header.display }}</th>
        </tr>
      </thead>
      <tbody>
        <tr :key="column.name" v-for="column in columns">
          <td :key="index" v-for="(header, index) in headers">
            {{ column[header.name] }}
          </td>
        </tr>
      </tbody>
      <tfoot>
        <tr>
          <th scope="col"> </th>
          <th scope="col">Итоговая сумма</th>
          <th scope="col">50</th>
          <th scope="col">24</th>
          <th scope="col">288</th>
          <th scope="col">46300</th>
          <th scope="col">555600</th>
        </tr>
      </tfoot>
    </table>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
  },
  data() {
    return {
      headers: [
        { name: 'number', display: '№' },
        { name: 'name', display: 'Наименование' },
        { name: 'quantity', display: 'Колличество' },
        { name: 'monthlyConsumption', display: 'Расход за месяц' },
        { name: 'yearlyConsumption', display: 'Расход за год' },
        { name: 'monthlyPrice', display: 'Цена за месяц (руб)' },
        { name: 'yearlyPrice', display: 'Цена за год (руб)' },
        { name: 'note', display: 'Примечание' }
      ],
      columns: [
        {
          number: "1",
          name: "Бумага офисная А4",
          quantity: "10 пачек",
          monthlyConsumption: "2 пачки",
          yearlyConsumption: "24 пачки",
          monthlyPrice: "800",
          yearlyPrice: "9 600",
          note: "Белая, 80 г/м²"
        },
        {
          number: "2",
          name: "Картридж для принтера HP 85A",
          quantity: "5 шт",
          monthlyConsumption: "0.3 шт",
          yearlyConsumption: "4 шт",
          monthlyPrice: "1 200",
          yearlyPrice: "14 400",
          note: "Оригинальный"
        },
        {
          number: "3",
          name: "Ручка шариковая синяя",
          quantity: "100 шт",
          monthlyConsumption: "15 шт",
          yearlyConsumption: "180 шт",
          monthlyPrice: "450",
          yearlyPrice: "5 400",
          note: "Офисные"
        },
        {
          number: "4",
          name: "Кофе молотый",
          quantity: "3 кг",
          monthlyConsumption: "1.5 кг",
          yearlyConsumption: "18 кг",
          monthlyPrice: "2 500",
          yearlyPrice: "30 000",
          note: "Jacobs Monarch"
        },
        {
          number: "5",
          name: "Бумага для факса",
          quantity: "8 рулонов",
          monthlyConsumption: "1 рулон",
          yearlyConsumption: "12 рулонов",
          monthlyPrice: "600",
          yearlyPrice: "7 200",
          note: "57мм х 30м"
        },
        {
          number: "6",
          name: "Маркеры перманентные",
          quantity: "20 шт",
          monthlyConsumption: "3 шт",
          yearlyConsumption: "36 шт",
          monthlyPrice: "900",
          yearlyPrice: "10 800",
          note: "Черные, тонкие"
        },
        {
          number: "7",
          name: "Скотч упаковочный",
          quantity: "12 шт",
          monthlyConsumption: "2 шт",
          yearlyConsumption: "24 шт",
          monthlyPrice: "480",
          yearlyPrice: "5 760",
          note: "45мм х 50м"
        },
        {
          number: "8",
          name: "Блокноты А5",
          quantity: "25 шт",
          monthlyConsumption: "4 шт",
          yearlyConsumption: "48 шт",
          monthlyPrice: "800",
          yearlyPrice: "9 600",
          note: "В клетку, 80 листов"
        },
        {
          number: "9",
          name: "Папки-скоросшиватели",
          quantity: "30 шт",
          monthlyConsumption: "5 шт",
          yearlyConsumption: "60 шт",
          monthlyPrice: "750",
          yearlyPrice: "9 000",
          note: "Пластиковые, А4"
        },
        {
          number: "10",
          name: "Тонер для копировального аппарата",
          quantity: "4 шт",
          monthlyConsumption: "0.5 шт",
          yearlyConsumption: "6 шт",
          monthlyPrice: "3 500",
          yearlyPrice: "42 000",
          note: "Canon 045"
        }
      ]
    }
  },
  methods: {
    output() {
      console.log(this.columns[2]);
      console.log(this.columns[4].quantity);
      return undefined
    }
  },
  mounted() {
    this.output()
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

table {
  width: 90%;
  margin: 0 auto;
  border-collapse: collapse;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  font-size: 16px;
  background-color: #fff;
  border-radius: 8px;
  overflow: hidden;
}

caption {
  caption-side: top;
  margin-bottom: 15px;
  font-size: 1.5em;
  font-weight: 600;
  color: #2c3e50;
}

thead {
  background-color: #4a90e2;
  color: white;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

thead th {
  padding: 12px 15px;
  border-right: 1px solid rgba(255, 255, 255, 0.3);
}

thead th:last-child {
  border-right: none;
}

tbody tr:nth-child(even) {
  background-color: #f4f7fc;
}

tbody td {
  padding: 12px 15px;
  border-bottom: 1px solid #e1e8f0;
  color: #333;
  text-align: center;
}

tbody td:first-child,
tbody td:nth-child(2) {
  text-align: left;
  padding-left: 20px;
}

tbody tr:hover {
  background-color: #dbeeff;
  cursor: pointer;
}

tfoot {
  background-color: #eaf1fb;
  font-weight: 600;
  color: #2c3e50;
}

tfoot th {
  padding: 12px 15px;
  border-top: 2px solid #4a90e2;
  text-align: center;
}

tfoot th:first-child {
  text-align: left;
  padding-left: 20px;
}
</style>
