// NOTE this solves part 2, I forgot to make a new file for part 2 and instead just edited this file

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

std::vector<std::vector<int>> loadData() {

    std::ifstream file;
    file.open("input.txt");
    if (!file.is_open()) {
        std::cout << "Failed to open input.txt\n";
        exit(1);
    }

    std::vector<std::vector<int>> reports;

    std::string line;
    while (file) {
        std::getline(file, line);

        std::vector<int> report;
        
        std::istringstream stream(line);
        std::string token;

        while (std::getline(stream, token, ' ')) {
            report.push_back(std::stoi(token));
        }

        reports.push_back(report);
    }

    return reports;
}

bool validateReport(std::vector<int> report, int index) {
    report.erase(report.begin() + index);

    if (report.size() == 0) {
        return false;
    }

    int direction = report.at(0) - report.at(1) >= 0 ? 1 : -1;

    for (int i = 0; i < report.size() - 1; i++) {
        int diff = (report.at(i) - report.at(i + 1)) * direction;
        if (!(diff >= 1) || !(diff <= 3)) {
            return false;
        }
    }

    return true;
}

int main() {
    std::vector<std::vector<int>> reports = loadData();

    int validReports = 0;
    for (auto report : reports) {
        for (int i = 0; i < report.size(); i++) {
            if (validateReport(report, i)) {
                validReports++;
                break;
            }
        }
    }

    std::cout << validReports << '\n';
}
