function buildMetadata(sample) {

    var url = `/metadata/${sample}`;

    

d3.json(url).then(function (response) {

        var data = response;

        var panel = d3.select("#sample-metadata");

        panel.html("");

        for (var key in data) {

            tag = document.createElement("h4");

            text = document.createTextNode(`${key}: ${data[key]}`);

            tag.append(text);

            panel.appendChild(tag);

         }

});



function buildCharts(sample) {



    var url = `samples/${sample}`;



    d3.json(url).then(function (response) {

        var data = response[0];



        var bubbletrace = [{

            x: data.otu_ids,

            y: data.sample_values,

            mode: "markers",

            marker: {

                size: response.sample_values,

                color: response.otu_ids

            },

            type: "scatter"

        }];



        var bubblelayout = {

            showlegend: false,

            height: 400,

            width: 1200

        };

        var bubble = document.getElementById('bubble');

        Plotly.plot(bubble, bubbletrace, bubblelayout)
        

        var pietrace = [{

            values: data.sample_values.slice(0, 10),

            labels: data.otu_ids.slice(0, 10),

            hoverinfo: data.otu_labels.slice(0, 10),

            type: "pie"

        }];



        var pielayout = {

            title: false;

            height: 375,

            width: 500

        };

        var pie = document.getElementById('pie');

        Plotly.plot(pie, pietrace, pielayout)

    });



}



function init() {


  var selector = d3.select("#selDataset");



  d3.json("/names").then((sampleNames) => {

    sampleNames.forEach((sample) => {

      selector

        .append("option")

        .text(sample)

        .property("value", sample);

    });



   

    const firstSample = sampleNames[0];

    buildCharts(firstSample);

    buildMetadata(firstSample);

  });

}



function optionChanged(newSample) {

  buildCharts(newSample);

  buildMetadata(newSample);

}



// Initialize the dashboard

init();}