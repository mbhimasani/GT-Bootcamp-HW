var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
var svg = d3
  .select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

var chartGroup = svg
  .append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`)
  .classed('chart', true);

// Import Data
d3.csv("assets/data/data.csv")
  .then(function(censusData) {

    // Parse Data/Cast as numbers
    // ==========================
    censusData.forEach(function(data) {
      data.id = +data.id;
      data.poverty = +data.poverty;
      data.povertyMoe = +data.povertyMoe;
      data.age = +data.age;
      data.ageMoe = +data.ageMoe;
      data.income = +data.income;
      data.incomeMoe = +data.incomeMoe;
      data.healthcare = +data.healthcare;
      data.healthcareLow = +data.healthcareLow;
      data.healthcareHigh = +data.healthcareHigh;
      data.obesity = +data.obesity;
      data.obesityLow = +data.obesityLow;
      data.obesityHigh = +data.obesityHigh;
      data.smokes = +data.smokes;
      data.smokesLow = +data.smokesLow;
      data.smokesHigh = +data.smokesHigh
    });
    console.log(censusData);

    // Create Scale Functions
    var xLinearScale = d3.scaleLinear()
      .domain([28, d3.max(censusData, d => d.age)])
      .range([0, width]);

    var yLinearScale = d3.scaleLinear()
      .domain([8, d3.max(censusData, d => d.smokes)])
      .range([height, 0]);

    // Create Axes functions
    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);

    // Append Axes to svg
    chartGroup.append("g")
      .attr("transform", `translate(0, ${height})`)
      .call(bottomAxis);

    chartGroup.append("g")
      .call(leftAxis);

    // Create circles
    var circlesGroup = chartGroup
      .selectAll("circle")
      .data(censusData)
      .enter()
      .append("circle")
      .attr("cx", d => xLinearScale(d.age))
      .attr("cy", d => yLinearScale(d.smokes))
      .attr("r", "10")
      .classed('stateCircle', true)
      .attr("opacity", ".5");

    // Add State Abbr in circles
    var text = chartGroup
      .selectAll("null")
      .data(censusData)
      .enter()
      .append("text")
      .attr("x", d => xLinearScale(d.age))
      .attr("y", d => yLinearScale(d.smokes)+3)
      .text(d => d.abbr)
      .classed('stateText', true)
      .attr("font-size", "10px");

    // Axes Labels
    chartGroup.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left + 40)
      .attr("x", 0 - (height / 2))
      .attr("dy", "1em")
      .classed('aText', true)
      .text("Smokers");

    chartGroup.append("text")
      .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
      .classed('aText', true)
      .text("Age");
});
