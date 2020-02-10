 use std::cmp::max;

pub fn time_between_two_dots(a:&Vec<i32>, b:&Vec<i32>) -> i32 {
    
    
     let x_diff = if a[0] > b[0] {a[0] - b[0]} else {b[0] - a[0]};
     let y_diff = if a[1] > b[1] {a[1] - b[1]} else {b[1] - a[1]};
    
    if a[0] == b[0] {
        return y_diff
    }
    if a[1] == b[1] {
        return x_diff
    }
     
     if x_diff == y_diff {
         return x_diff
     } 
     max(x_diff, y_diff)
 }

impl Solution {
     pub fn min_time_to_visit_all_points(points: Vec<Vec<i32>>) -> i32 {
        let mut time:i32 = 0;
        let counter:usize = 0;
        
        for counter in 0..points.len()-1 {
            time += time_between_two_dots(&points[counter], &points[counter+1]);
        }
        time
    }
}
