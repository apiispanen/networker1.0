navigator.mediaDevices.getUserMedia({ audio: true })
  .then(function (stream) {
    var audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    var source = audioCtx.createMediaStreamSource(stream);

    // send the audio data to the Python script
    // Create a new instance of XMLHttpRequest
    var xhr = new XMLHttpRequest();

    // Open the request and specify the URL and method
    xhr.open("POST", "http://127.0.0.1:5000", true);

    // Set the request header to indicate that we're sending audio data
    xhr.setRequestHeader("Content-Type", "application/octet-stream");

    // Send the audio data to the Python script
    xhr.send(audioData);



  })
  .catch(function (error) {
    console.error("Error accessing microphone: ", error);
  });
