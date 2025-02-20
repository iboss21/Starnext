
import os
import sys
import subprocess
import importlib

# List of all modular blocks to be installed
modules = [
    'navigation_block',
    'defense_block',
    'life_support_block',
    'communication_block',
    'medical_block',
    'scanning_block',
    'power_management_block',
    'ai_behavior_block',
    'cloak_stealth_block',
    'alien_detection_block',
    'anomaly_detection_block',
    'exploration_block',
    'advanced_defense_block',
    'cyberwarfare_block',
    'repair_block',
    'fabrication_block',
    'alien_integration_block',
    'adaptive_ship_block',
    'economy_block',
    'history_culture_block',
    'language_translation_block',
    'law_drafting_block',
    'financial_management_block',
    'religion_block',
    'entertainment_block',
    'diy_databank_block',
    'self_sufficiency_block',
    'psychological_wellbeing_block',
    'knowledge_skills_block'
]

def check_module_installed(module_name):
    """
    Check if the module already exists on the system.
    """
    return os.path.isfile(f"{module_name}.py")

def install_module(module_name):
    """
    Installs a module by creating the file if it's not already installed.
    """
    try:
        print(f"Installing module: {module_name}")
        with open(f"{module_name}.py", 'w') as f:
            f.write(f"# This is the module for {module_name}\n")
            f.write("def initialize():\n")
            f.write(f"    print('{module_name} initialized')\n")
    except Exception as e:
        print(f"Failed to install {module_name}: {str(e)}")
        sys.exit(1)

def initialize_ai():
    """
    Initialize the AI and check for missing modules.
    """
    print("Initializing STARNEX AI...")

    # Check and install missing modules
    for module in modules:
        if not check_module_installed(module):
            install_module(module)
        else:
            print(f"Module {module} already installed.")

    # Once all modules are installed, run initialization for each
    for module in modules:
        try:
            module_import = importlib.import_module(module)
            module_import.initialize()
        except Exception as e:
            print(f"Failed to initialize {module}: {str(e)}")

    print("STARNEX AI setup complete.")

if __name__ == "__main__":
    initialize_ai()
