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
          <th scope="col"></th>
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
import axios from 'axios';

export default {
  name: 'App',
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
      columns: [] // Теперь данные будут приходить с бэкенда
    };
  },
  async mounted() {
    try {
      const response = await axios.get('http://localhost:5000/api/data'); // URL вашего Flask бэкенда
      this.columns = response.data;
    } catch (error) {
      console.error('Ошибка при получении данных:', error);
    }
  }
};
</script>

<style>
/* Ваши стили остаются без изменений */
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