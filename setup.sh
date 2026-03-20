#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${CYAN}${BOLD}"
echo "════════════════════════════════════════════════════════════"
echo "          ERROR ENCRYPTOR - INSTALLER & LAUNCHER"
echo "════════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${BLUE}[1/3] Checking Python...${NC}"
if command -v python3 &> /dev/null; then
    echo -e "${GREEN}✅ Python3 found${NC}"
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    echo -e "${GREEN}✅ Python found${NC}"
    PYTHON_CMD="python"
else
    echo -e "${RED}❌ Python not installed!${NC}"
    echo -e "${YELLOW}Installing Python...${NC}"
    if command -v pkg &> /dev/null; then
        pkg update && pkg install python -y
    elif command -v apt &> /dev/null; then
        sudo apt update && sudo apt install python3 -y
    else
        echo -e "${RED}Failed to install Python${NC}"
        exit 1
    fi
fi

echo -e "${BLUE}[2/3] Checking pip...${NC}"
if command -v pip3 &> /dev/null || command -v pip &> /dev/null; then
    echo -e "${GREEN}✅ pip found${NC}"
else
    echo -e "${YELLOW}Installing pip...${NC}"
    $PYTHON_CMD -m ensurepip --upgrade
fi

echo -e "${BLUE}[3/3] Checking script...${NC}"
if [ -f "Error_Encryptor.py" ]; then
    echo -e "${GREEN}✅ Error_Encryptor.py found${NC}"
else
    echo -e "${RED}❌ Error_Encryptor.py not found!${NC}"
    echo -e "${YELLOW}Please place Error_Encryptor.py in current directory${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}${BOLD}✅ ALL SET!${NC}"
echo ""

echo -e "${CYAN}════════════════════════════════════════════════════════════${NC}"
echo -e "${YELLOW}🚀 Launching ERROR ENCRYPTOR...${NC}"
echo -e "${CYAN}════════════════════════════════════════════════════════════${NC}"
echo ""

$PYTHON_CMD Error_Encryptor.py