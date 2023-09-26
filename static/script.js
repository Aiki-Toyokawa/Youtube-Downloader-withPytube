function downloadVideo() {
  const videoUrl = document.getElementById("videoUrl").value;
  const downloadStatus = document.getElementById("downloadStatus");

  downloadStatus.textContent = "Downloading...";

  fetch(`/download?videoUrl=${encodeURIComponent(videoUrl)}`)
      .then(response => response.json())
      .then(data => {
          if (data.error) {
              downloadStatus.textContent = "Error: " + data.error;
          } else {
              downloadStatus.textContent = "Video downloaded successfully!";
              const thumbnail = document.getElementById("thumbnail");
              thumbnail.src = data.thumbnailUrl;
              thumbnail.style.display = "block";
          }
      })
      .catch(error => {
          downloadStatus.textContent = "Error: " + error.message;
      });
}
