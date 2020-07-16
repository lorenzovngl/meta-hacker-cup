<?php
/**
 * Code written by Lorenzo Vainigli for Facebook Hacker Cup 2017 Qualification Round
 * This program was verified correct, source:
 * https://www.facebook.com/codingcompetitions/hacker-cup/2017/qualification-round/scoreboard?start=8880
**/

ini_set('max_execution_time', 300); // 5 minutes

$main_name = "progress_pie";
$input_filename = $main_name . "_example_input.txt";
$output_filename = $main_name . "_example_output.txt";
$input_filename = $main_name . ".txt";
$output_filename = $main_name . "_output.txt";

$input_file = file_get_contents($input_filename);
$output_file = fopen($output_filename, "w");
$matches = array();
preg_match_all("/([0-9])+/i", $input_file, $matches);
$data = array();
foreach ($matches[0] as $value) {
    array_push($data, intval($value));
}
$cursor = 0;
$T = $data[$cursor];
$cursor++;
//echo "Number of cases: " . $T . PHP_EOL;
$points_of_circle = array();
for ($j = 0; $j <= 100; $j++) {
    $a = $j * 3.6;
    $sin = round(sin(deg2rad($a)) * 50 + 50, 6);
    $cos = round(cos(deg2rad($a)) * 50 + 50, 6);
    array_push($points_of_circle, ["x" => $sin, "y" => $cos]);
}
$i = 1;
while ($i <= $T) {
    $start_time = microtime(true);
    $P = $data[$cursor];
    $cursor++;
    $X = $data[$cursor];
    $cursor++;
    $Y = $data[$cursor];
    $cursor++;
    //echo $P . "%, X = " . $X . " Y = " . $Y . PHP_EOL;
    $color = 0; // 0 = white, 1 = black;
    // The point is in the circle? If not, it must be white
    // (x-x1)^2+(y-y1)^2 = r^2 with r = 50
    $isInner = pow($X - 50, 2) + pow($Y - 50, 2) <= pow(50, 2);
    if ($isInner) {
        if ($P == 0) {
            $color = 0;
        } else if ($P == 100) {
            $color = 1;
        } else {
            // The point is in the filled-black area?
            // ((x-x1)/(x2-x1)) = ((y-y1)/(y2-y1)) with x1 = 50 && x2 = 50
            $x_2 = $points_of_circle[$P]["x"];
            $y_2 = $points_of_circle[$P]["y"];
            // Find in which area (X,Y) is located
            if ($X >= 50){
                if ($Y >= 50){
                    // Area 0-25
                    if ($P >= 25){
                        $color = 1;
                    } else {
                        if ($x_2 == 50){
                            $cond = $X >= 50;
                        } else if ($y_2 == 50){
                            $cond = $Y >= 50;
                        } else {
                            $cond = (($X-50)/($x_2-50)) <= (($Y-50)/($y_2-50));
                        }
                        if ($cond){
                            $color = 1;
                        } else {
                            $color = 0;
                        }
                    }
                } else {
                    // Area 25-50
                    if ($P <= 25) {
                        $color = 0;
                    } else if ($P >= 50) {
                        $color = 1;
                    } else {
                        if ($x_2 == 50){
                            $cond = $X >= 50;
                        } else if ($y_2 == 50){
                            $cond = $Y <= 50;
                        } else {
                            $cond = (($X-50)/($x_2-50)) >= (($Y-50)/($y_2-50));
                        }
                        if ($cond){
                            $color = 1;
                        } else {
                            $color = 0;
                        }
                    }
                }
            } else {
                if ($Y <= 50){
                    // Area 50-75
                    if ($P <= 50){
                        $color = 0;
                    } else if ($P >= 75){
                        $color = 1;
                    } else {
                        if ($x_2 == 50){
                            $cond = $X <= 50;
                        } else if ($y_2 == 50){
                            $cond = $Y <= 50;
                        } else {
                            $cond = (($X-50)/($x_2-50)) <= (($Y-50)/($y_2-50));
                        }
                        if ($cond){
                            $color = 1;
                        } else {
                            $color = 0;
                        }
                    }
                } else {
                    // Area 75-100
                    if ($P <= 75){
                        $color = 0;
                    } else {
                        if ($x_2 == 50){
                            $cond = $X <= 50;
                        } else if ($y_2 == 50){
                            $cond = $Y >= 50;
                        } else {
                            $cond = (($X-50)/($x_2-50)) >= (($Y-50)/($y_2-50));
                        }
                        if ($cond){
                            $color = 1;
                        } else {
                            $color = 0;
                        }
                    }
                }
            }
        }
    } else {
        $color = 0;
    }
    fwrite($output_file, "Case #".$i.": ".($color ? "black" : "white").PHP_EOL);
    $end_time = microtime(true);
    $spent_time = $end_time - $start_time;
    //echo "Case #".$i.": ".($color ? "black" : "white") ." in ". $spent_time.PHP_EOL;
    $i++;
}
fclose($output_file);
