import buffons_needle as bn1
import buffons_needle2 as bn2

def main():
    print("="*90)
    print("=== Experiment 1 : Standart Buffon's Needle ===")
    bn1.run_experiment()
    print("="*90)
    
    print("\n" + "="*90)
    print("=== Experiment 2 : Radial Buffon's Needle ===")
    print("="*90)
    bn2.run_experiments()

if __name__ == "__main__":
    main()