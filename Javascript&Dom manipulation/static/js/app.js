// from data.js
var tableData = data;
var tbody = document.getElementById('tbody');
//
console.log(tableData);
generateRows(tableData);


// filtering
var submit = d3.select("#filter-btn");

submit.on("click", function() {

  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#filter");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");

  console.log(inputValue);

  var filteredData = tableData.filter(function(d) {

    if( d.datetime === inputValue || d.city === inputValue || d.state === inputValue || d.country === inputValue || d.shape === inputValue)
    {
      return d
    };
  });
  tbody.innerHTML = "";
  generateRows(filteredData);
  console.log(filteredData);
});


// version one with pure javascript:
function generateRows(data) {
  data.forEach((d) => {
    var row = document.createElement('tr');
    row.innerHTML=`<td>${d.datetime}</td><td>${d.city}</td><td>${d.state}</td><td>${d.country}</td><td>${d.shape}</td><td>${d.durationMinutes}</td><td>${d.comments}</td>`;
    tbody.appendChild(row);
  });
};









// version two using d3 elements and javascript: but this does not have the bootstrap table-striped styling applied. not sure why. any advice or hints?
// var tbody = d3.select("tbody");
// tableData.forEach((UFOsightings) => {
//   var row = tbody.append("tr");
//   Object.entries(UFOsightings).forEach(([key, value]) => {
//     var cell = tbody.append("td");
//     cell.text(value);
//   });
// });

// using D3 library:
// d3.select("tbody")
//   .selectAll("tr")
//   .data(data)
//   .enter()
//   .append("tr")
//   .html(function(d) {
//     return `<td>${d.datetime}</td><td>${d.city}</td><td>${d.state}</td><td>${d.country}</td><td>${d.shape}</td><td>${d.durationMinutes}</td><td>${d.comments}</td>`;
//   });
