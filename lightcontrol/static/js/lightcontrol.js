document.addEventListener('DOMContentLoaded', function() {
    var toggleButton = document.getElementById('toggleButton');
    var autoModeButton = document.getElementById('autoModeButton');
    var ledStateDisplay = document.getElementById('ledState');
    var autoModeStateDisplay = document.getElementById('autoModeState');
    var ledIndicator = document.getElementById('ledIndicator');
    var autoModeIndicator = document.getElementById('autoModeIndicator');
    var pollingInterval;

    // Function to update the LED state display and indicator
    function updateLedState(state) {
        ledStateDisplay.textContent = state ? 'On' : 'Off';
        if(state) {
            ledIndicator.classList.remove('led-off');
            ledIndicator.classList.add('led-on');
            toggleButton.classList.add('btn-success');
        } else {
            ledIndicator.classList.remove('led-on');
            ledIndicator.classList.add('led-off');
            toggleButton.classList.remove('btn-success');
        }
    }

    // Function to update the Auto Mode state display and button text
    function updateAutoModeState(state) {
        autoModeStateDisplay.textContent = state ? 'On' : 'Off';
        if(state) {
            autoModeIndicator.classList.remove('led-off');
            autoModeIndicator.classList.add('led-on');
            autoModeButton.classList.add('btn-success');
        } else {
            autoModeIndicator.classList.remove('led-on');
            autoModeIndicator.classList.add('led-off');
            autoModeButton.classList.remove('btn-success');
        }
    }

    function pollLdrAndUpdateLed() {
        fetch('/lightcontrol/control_led_with_ldr/', { method: 'GET' })
            .then(response => response.json())
            .then(data => {
                updateLedState(data.led_state);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    }

    // Function to handle the toggle button click
    toggleButton.addEventListener('click', function() {
        fetch('/lightcontrol/toggle/', { method: 'GET' })
            .then(response => response.json())
            .then(data => {
                updateLedState(data.led_state);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    });

    // Function to handle the auto mode button click
    autoModeButton.addEventListener('click', function() {
        fetch('/lightcontrol/toggle_auto_mode/', { method: 'GET' })
            .then(response => response.json())
            .then(data => {
                updateAutoModeState(data.auto_mode);
                if (data.auto_mode) {
                    // Auto Mode is now ON, start polling
                    pollingInterval = setInterval(pollLdrAndUpdateLed, 5000); // Poll every 5 seconds
                } else {
                    // Auto Mode is now OFF, stop polling
                    clearInterval(pollingInterval);
                }
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    });

    // Initial check of the LED state when the page loads
    fetch('/lightcontrol/state/', { method: 'GET' })
        .then(response => response.json())
        .then(data => {
            updateLedState(data.led_state);
        })
        .catch((error) => {
            console.error('Error:', error);
        });

    // Initial check of the Auto Mode state when the page loads
    fetch('/lightcontrol/auto_mode_state/', { method: 'GET' })
        .then(response => response.json())
        .then(data => {
            updateAutoModeState(data.auto_mode);
        })
        .catch((error) => {
            console.error('Error:', error);
        });

    window.addEventListener('beforeunload', function() {
        clearInterval(pollingInterval);
    });
});
