use std::{collections::HashMap, fs::File, io::Read, io};

fn load_data() -> Result<(Vec<i32>, Vec<i32>), io::Error> {
    let mut file = File::open("01/input.txt")?;

    let mut contents = String::new();
    file.read_to_string(&mut contents)?;

    let mut col1: Vec<i32> = Vec::new();
    let mut col2: Vec<i32> = Vec::new();

    for (i, line) in contents.lines().enumerate() {
        let mut parts = line.split_whitespace();

        let part1 = parts.next().ok_or_else(
            || io::Error::new(io::ErrorKind::InvalidData, format!("Missing first number on line {}", i + 1)
        ))?;

        let part2 = parts.next().ok_or_else(
            || io::Error::new(io::ErrorKind::InvalidData, format!("Missing second number on line {}", i + 1)
        ))?;

        let num1 = part1.parse::<i32>().map_err(
            |_| io::Error::new(io::ErrorKind::InvalidData, format!("Invalid first number '{}' on line {}", part1, i + 1)
        ))?;

        let num2 = part2.parse::<i32>().map_err(
            |_| io::Error::new(io::ErrorKind::InvalidData, format!("Invalid second number '{}' on line {}", part2, i + 1)
        ))?;

        col1.push(num1);
        col2.push(num2);
    }

    Ok((col1, col2))
}

fn main() {
    match load_data() {
        Ok((col1, col2)) => {
            let mut total: i32 = 0;

            let mut frequency: HashMap<i32, i32> = HashMap::new();
            for &num in col2.iter() {
                *frequency.entry(num).or_insert(0) += 1;
            }

            for num1 in col1.iter() {
                total += num1 * frequency.get(&num1).unwrap_or(&0);
            }

            println!("Total: {}", total);
        }

        Err(e) => eprintln!("Error: {}", e),
    }
}
