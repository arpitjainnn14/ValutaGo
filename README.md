# ValutaGo - Modern Currency Converter

A beautiful, responsive web application for real-time currency conversion built with Flask and modern web technologies.

![ValutaGo Screenshot](static/screenshot.png)

## 🌟 Features

- **Real-time Currency Conversion**: Get instant currency conversion rates using the ExchangeRate-API
- **Modern UI/UX**: Clean, responsive design with smooth animations
- **Comprehensive Currency Support**: Access to 170+ global currencies
- **Interactive Sidebar**: Easy currency selection with search functionality
- **About Section**: Learn about the project and developer
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Real-time Updates**: AJAX-powered conversion without page reload
- **Beautiful Animations**: Smooth transitions and hover effects

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **APIs**: ExchangeRate-API
- **Libraries**: 
  - Bootstrap 5.3.0
  - Font Awesome 6.0.0
  - jQuery 3.6.0

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/valutago.git
cd valutago
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your API key:
   - Get an API key from [ExchangeRate-API](https://www.exchangerate-api.com/)
   - Update the `API_KEY` variable in `app.py`

### Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## 💻 Usage

1. **Currency Conversion**:
   - Enter the amount to convert
   - Select source currency (From)
   - Select target currency (To)
   - Click "Convert" or press Enter
   - View the conversion result

2. **Currency Selection**:
   - Use the sidebar to browse available currencies
   - Search currencies using the search box
   - Click on a currency to select it

3. **About Section**:
   - Click "About ValutaGo" to learn more about the project
   - View developer information and contact details

## 📱 Responsive Design

- **Desktop**: Full sidebar with search functionality
- **Tablet**: Collapsible sidebar with touch support
- **Mobile**: Optimized layout with mobile-friendly controls

## 🎨 Customization

### Styling
- Colors can be customized by modifying the CSS variables in the style sections
- Main colors are defined in the `:root` selector
- Animations can be adjusted in the keyframes sections

### Adding Currencies
- Currency codes and names are defined in the `CURRENCY_CODES` dictionary in `app.py`
- Add or modify currencies by updating this dictionary

## 👨‍💻 Developer Information

- **Developer**: Arpit Jain
- **Contact**: [Your Email]
- **GitHub**: [Your GitHub]
- **LinkedIn**: [Your LinkedIn]

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- ExchangeRate-API for providing the currency conversion data
- Bootstrap and Font Awesome for the UI components
- Flask team for the amazing web framework

## 🔄 Updates

- Added responsive design
- Implemented real-time currency conversion
- Added beautiful animations
- Created about page
- Enhanced UI/UX with modern design elements

---

Made with ❤️ by Arpit Jain 