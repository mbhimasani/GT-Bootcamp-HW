function buildMetadata(sample) {
  // @TODO: Complete the following function that builds the metadata panel
  var url = `/metadata/${sample}`;

  // Use `d3.json` to fetch the metadata for a sample
  d3.json(url).then((metadata) => {

    // Use d3 to select the panel with id of `#sample-metadata`
    var sampleMetadata = d3.select("#sample-metadata");

    // Use `.html("") to clear any existing metadata
    sampleMetadata.html("");

    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.
    Object.entries(metadata).forEach(([key, value]) => {
      console.log(key, value);
      var row = sampleMetadata.append("panel-body");
      row.text(`${key}: ${value} \n`);
    });
    // BONUS: Build the Gauge Chart
    buildGauge(metadata.WFREQ);
  });
}

function buildCharts(sample) {
  var url = `/samples/${sample}`;
  // @TODO: Use `d3.json` to fetch the sample data for the plots
  d3.json(url).then((sampleData) => {

    // @TODO: Build a Bubble Chart using the sample data
    var x_values = sampleData.otu_ids;
    var y_values = sampleData.sample_values;
    var marker_size = sampleData.sample_values;
    var marker_colors = sampleData.otu_ids;
    var text_values = sampleData.otu_labels;

    var trace1 = {
      x: x_values,
      y: y_values,
      text: text_values,
      mode: 'markers',
      marker: {
        color: marker_colors,
        colorscale: 'rainbow',
        size: marker_size
      }
    };

    var data1 = [trace1];

    var layout = {
      xaxis: { title: "OTU ID" }
    };

    Plotly.newPlot('bubble', data1, layout);

    // @TODO: Build a Pie Chart
    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
    var pie_values = sampleData.sample_values.slice(0, 10);
    var pie_labels = sampleData.otu_ids.slice(0, 10);
    var pie_text = sampleData.otu_labels.slice(0, 10);

    var data2 = [{
      values: pie_values,
      labels: pie_labels,
      hovertext: pie_text,
      type: 'pie'
    }];

    Plotly.newPlot('pie', data2);
  });
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
