# Setting Up OPENAI_API_KEY

## 🔑 Quick Setup

### Option 1: Set for Current Session
```bash
export OPENAI_API_KEY='your-api-key-here'
```

### Option 2: Set Permanently (Recommended)
Add to your `~/.bashrc` or `~/.zshrc`:
```bash
echo 'export OPENAI_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

### Option 3: Use .env File
Create a `.env` file in the project root:
```bash
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

Then load it:
```bash
source venv/bin/activate
export $(cat .env | xargs)
```

## ✅ Verify API Key is Set

```bash
echo $OPENAI_API_KEY
```

If it shows your key, you're good to go!

## 🧪 Test with API Key

Once set, run the interactive test script:
```bash
cd /mnt/sdb1/dspy_test
source venv/bin/activate
./test_one_by_one.sh
```

The script will:
1. Check if API key is set
2. Prompt you to set it if missing
3. Test each problem one by one
4. Wait for your confirmation between problems

## 📝 Notes

- **Without API key**: Examples will use mocks (still runnable)
- **With API key**: Real LLM calls will be made (costs apply)
- **Security**: Never commit your API key to git!

## 🔒 Security Best Practices

1. ✅ Use environment variables (not hardcoded)
2. ✅ Add `.env` to `.gitignore`
3. ✅ Use different keys for dev/prod
4. ✅ Rotate keys regularly

