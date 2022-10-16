/*======== Google Map chart ========*/
google.charts.load('current', {
  'packages':['geochart'],
});
google.charts.setOnLoadCallback(drawRegionsMap);

function drawRegionsMap() {
  var data = google.visualization.arrayToDataTable([
    ['Country', 'Purchased'],
    ['Germany', 50],
    ['United States', 300],
    ['Brazil', 400],
    ['Canada', 500],
    ['France', 600],
['India', 987],
    ['RU', 700]
  ]);

  var options = {
colorAxis: {colors: ['#cedbf9', '#6588d5']},
};

  var chart = new google.visualization.GeoChart(document.getElementById('regions_purchase'));

  chart.draw(data, options);
}