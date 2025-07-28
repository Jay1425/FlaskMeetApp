# Video Calling Web App with Flask

A real-time video calling web application built with Flask, Socket.IO, and WebRTC.

## Features

- 🎥 **HD Video Quality** - High-definition video calls
- 🎤 **Crystal Clear Audio** - High-quality audio communication
- 🔒 **Secure Connection** - Secure peer-to-peer connections
- 📱 **Cross Platform** - Works on desktop and mobile devices
- 🖥️ **Screen Sharing** - Share your screen with participants
- 👥 **Multiple Participants** - Support for multiple users in a room
- 📋 **Easy Room Sharing** - Simple room ID system for easy joining

## Installation

1. **Clone or download this project**

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open your browser and navigate to:**
   ```
   http://localhost:5000
   ```

## How to Use

### Starting a Video Call

1. **Open the application** in your web browser
2. **Enter your name** in the "Your Name" field
3. **Create a new room** by clicking "Create New Room" or enter an existing room ID
4. **Click "Join Room"** to start your video call
5. **Share the room link** with others to invite them to join

### During a Call

- **Toggle Video**: Click the video button to turn your camera on/off
- **Toggle Audio**: Click the microphone button to mute/unmute
- **Share Screen**: Click the screen button to share your screen
- **Leave Call**: Click the red phone button to hang up and leave the room

### Inviting Others

- Copy the room link from the waiting screen and share it with participants
- Others can join by entering the same room ID on the home page
- The room supports multiple participants joining simultaneously

## Technical Details

### Architecture

- **Backend**: Flask with Socket.IO for real-time communication
- **Frontend**: HTML5, CSS3, JavaScript with WebRTC for peer-to-peer video
- **Real-time Communication**: Socket.IO handles signaling between peers
- **Video/Audio**: WebRTC handles direct peer-to-peer media streams

### Browser Requirements

- **Chrome/Chromium**: Full support
- **Firefox**: Full support
- **Safari**: Full support (iOS 14.3+)
- **Edge**: Full support

### Network Requirements

- **HTTPS**: Required for camera/microphone access (in production)
- **Firewall**: May need to open ports for WebRTC (usually automatic)
- **STUN Servers**: Uses Google's public STUN servers for NAT traversal

## Customization

### Changing the Secret Key

Edit the `app.py` file and change the secret key:

```python
app.config['SECRET_KEY'] = 'your-secure-secret-key-here'
```

### Adding HTTPS

For production deployment, configure HTTPS:

```python
if __name__ == '__main__':
    socketio.run(app, debug=False, host='0.0.0.0', port=5000, 
                ssl_context='adhoc')  # For development HTTPS
```

### Styling

The application uses CSS Grid and Flexbox for responsive design. You can customize the appearance by editing the `<style>` sections in the HTML templates.

## Deployment

### Local Network

To make the app accessible on your local network:

1. Find your local IP address
2. Run the app with `host='0.0.0.0'`
3. Access via `http://[your-ip]:5000`

### Production Deployment

For production deployment:

1. Use a proper WSGI server like Gunicorn
2. Configure HTTPS with SSL certificates
3. Use a reverse proxy like Nginx
4. Consider using TURN servers for better NAT traversal

## Troubleshooting

### Camera/Microphone Access

- **Permission Denied**: Allow camera/microphone access in browser settings
- **HTTPS Required**: Use HTTPS in production for media access
- **Device Busy**: Close other applications using camera/microphone

### Connection Issues

- **Firewall**: Check firewall settings
- **NAT**: Some corporate networks may block WebRTC
- **Browser Console**: Check for JavaScript errors

### Performance

- **Multiple Participants**: Performance depends on bandwidth and device capability
- **Screen Sharing**: May reduce video quality for other participants
- **Mobile Devices**: May have limitations on simultaneous streams

## Development

### Project Structure

```
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   ├── index.html     # Home page
│   └── room.html      # Video call room
└── README.md          # This file
```

### Adding Features

- **Chat**: Add text chat functionality using Socket.IO
- **Recording**: Implement call recording features
- **File Sharing**: Add file sharing capabilities
- **User Authentication**: Add login/registration system

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have questions:

1. Check the browser console for error messages
2. Ensure all dependencies are installed correctly
3. Verify camera/microphone permissions
4. Test with different browsers

## Author

**Created by Jay Raychura**
**Designed by Pujan Chudasama**

---

**Made with ❤️ using Flask, Socket.IO, and WebRTC**
