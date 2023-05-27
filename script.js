document.getElementById("scheduleForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission
  
    var studentID = document.getElementById("studentID").value;
  
    fetch("schedule.json")
      .then(function(response) {
        return response.json();
      })
      .then(function(scheduleData) {
        var scheduleDisplay = document.getElementById("scheduleDisplay");
        scheduleDisplay.innerHTML = ""; // Clear previous schedule display
  
        var found = false;
        var table = document.createElement("table");
        var tableHeaderRow = document.createElement("tr");
        var classNameHeader = document.createElement("th");
        classNameHeader.textContent = "Class Name";
        var classTimeHeader = document.createElement("th");
        classTimeHeader.textContent = "Class Time";
        tableHeaderRow.appendChild(classNameHeader);
        tableHeaderRow.appendChild(classTimeHeader);
        table.appendChild(tableHeaderRow);
  
        for (var i = 0; i < scheduleData.length; i++) {
          var classes = scheduleData[i].classes;
  
          for (var j = 0; j < classes.length; j++) {
            var classInfo = classes[j];
            var className = classInfo.className;
            var classTime = scheduleData[i].time;
            var eligibleRollNumbers = classInfo.eligibleRollNumbers;
  
            if (eligibleRollNumbers.includes(studentID)) {
              found = true;
              var tableRow = document.createElement("tr");
              var classNameCell = document.createElement("td");
              classNameCell.textContent = className;
              var classTimeCell = document.createElement("td");
              classTimeCell.textContent = classTime;
              classTimeCell.className = "timec"
              tableRow.appendChild(classNameCell);
              tableRow.appendChild(classTimeCell);
              table.appendChild(tableRow);
            }
          }
        }
  
        scheduleDisplay.appendChild(table);
  
        if (!found) {
          var noScheduleMsg = document.createElement("p");
          table.style.display = "none";
          noScheduleMsg.textContent = "No schedule found for the entered ID.";
          scheduleDisplay.appendChild(noScheduleMsg);
        }
      })
      .catch(function(error) {
        console.log("Error fetching schedule data:", error);
      });
  });
  
