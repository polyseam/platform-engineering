# 🧑‍💻 Dagger Hackathon: June 18th, 2025

Welcome to the Dagger hackathon hosted by the CNCF and Code to Cloud! By the end of this hack, you will have a good understanding of how to use Dagger and the various use cases it can help support.

## 🎯 Expected Outcomes

✅ Build a real-world use case with Dagger

✅ Dagger pipeline runs unit tests

✅ Dagger pipeline triggers LLM workflow if tests fail

✅ LLM provides feedback on why tests could be failing in a PR

## ✅ Prerequisites

There are two options for this hackathon. We highly recommend the first option to avoid dependency issues.

### 1️⃣ Option 1: Github Codespace

### 2️⃣ Option 2: Local

Make sure to follow the prerequisites defined [here](../README.md) in the main Dagger README.

## 🔨 Implementation

All the code for the below can be found [here](./dagger-hackathon-pipeline/).

Make sure you have the repo cloned and you are in the `docs\dagger\dagger-hackathon-pipeline` directory:

```bash
# Clone the repository from GitHub
git clone https://github.com/codetocloudorg/platform-engineering.git

# Change directory to the Dagger hackathon pipeline documentation folder
cd ./docs/dagger/dagger-hackathon-pipeline
```

### Step 1: Create a Feature Branch

### 🤖 Step 2: Select your LLM Provider

### Step 3: Create a PR

### Step 4: Run the Dagger Function

## Gothcas
1. Sometimes the LLM that reviews the failed unit test logs returns a incorrect path to the file with breaking changes, incorrect line number of the breaking change, or incorrect fix (i.e. too verbose)
2. Current state of this does not work with multi-line code changes or multiple breaking changes. 1 breaking change on 1 line
3. The way commit id is retrieved is not robust - if I have a breaking change that is pushed to a branch with a open PR and it is commit id 1 and I then commit another file the latest commmit id becomes 2. The code is setup to grab latest commit id and not commit id of file causing breaking change so it will fail (i.e. no diff)