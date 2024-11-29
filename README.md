# Decision Making Calculator

A Python GUI application that helps you make decisions by comparing different alternatives using various decision-making methods.

## 🎯 What Does It Do?

This tool helps you when you:

- Have multiple choices (alternatives)
- Each choice has different possible outcomes
- Need help deciding which choice is best

## 🚀 Quick Start

1. **Install Python** (version 3.x)
2. **Run the program**:

```bash
python uncertaintyProject.py
```

## 📝 How to Use

### Step 1: Add Your Alternatives

1. Enter a name (e.g., "Job A")
2. Enter possible outcomes separated by commas (e.g., "50000, 60000, 45000")
3. Click "Add Alternative"

Example:

```
Name: Job A
Values: 50000, 60000, 45000

Name: Job B
Values: 45000, 65000, 55000
```

### Step 2: Choose a Decision Method

Pick one of these buttons:

- **Maximax** (The Optimist's Choice)

  - Looks at the best possible outcome
  - Good if you're feeling lucky!

- **Maximin** (The Cautious Choice)

  - Looks at the worst possible outcome
  - Good if you want to play it safe

- **Hurwicz** (The Balanced Choice)

  - Combines optimistic and pessimistic views
  - You choose how optimistic you want to be (0-1)

- **Laplace** (The Average Choice)
  - Takes the average of all outcomes
  - Good when all outcomes are equally likely

### Step 3: View Results

The program will show you:

- The calculated result
- Which alternative is best according to your chosen method

## 🛠️ Example Use Case

Deciding between two job offers:

```
Job A: Base salary + possible bonus
Values: 50000, 60000, 45000
(Base salary, Good year, Bad year)

Job B: Commission-based salary
Values: 45000, 65000, 55000
(Minimum, Maximum, Average)
```

## ⚠️ Common Errors and Fixes

| Error Message   | What It Means         | How to Fix                                          |
| --------------- | --------------------- | --------------------------------------------------- |
| "Missing Data"  | Empty name or values  | Fill in both fields                                 |
| "Invalid Input" | Wrong number format   | Use numbers and commas only (e.g., "100, 200, 300") |
| "No Data"       | No alternatives added | Add at least one alternative first                  |

## 💡 Tips

1. Add all your alternatives before calculating
2. Try different methods to see how they compare
3. Use realistic numbers for better results
4. Clear values = better decisions

## 🔧 Technical Requirements

- Python 3.x
- Tkinter (included with Python)
- Screen resolution: 800x600 or higher

## 🤝 Contributing

Found a bug? Have a suggestion? Please:

1. Fork the repository
2. Create a new branch
3. Submit a pull request

## 📄 License

This project is open source, under the MIT License.

## 👥 Support

Need help?

- Check the error messages
- Review the examples above
- [Create an issue](link-to-your-repository/issues)

---

Made with ❤️ for decision-makers everywhere

[Your Name/Organization]
