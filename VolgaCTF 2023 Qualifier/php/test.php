<?php

class UnfinishedСlass {
    public $handler;
    public function runMe()
    {
     if (!$this->handler->current()){
         return true;
     }else{
         throw Error;
     }
    }

}


class First{
    public $flag = true;
    public function runMe(){
        return $this->flag;
    }
}

class Second{
    public $flag = true;
    public $my_obj = array("trash1"=>"35");
    public function changeFlag(){
        $this->flag=true;
    }
    public function runMe(){
        if ($this->flag===true){
            echo $this->my_obj->trash1;
            return true;
        }
        else{
            return false;
        }
    }
}

class PlayGround{
    public function __construct(){
        $this->first = new First();
        $this->second = new Second();
        $this->third = new UnfinishedСlass();
    }
    public $first;
    public $second;
    public $third;
    public function __wakeup(){
        if ($this->first->runMe()){
            if ($this->second->runMe()){
                if ($this->third->runMe()){
                    echo 'VolgaCTF{your flag}';
                }
            }
        }
    }
}


$obj = new PlayGround();

$obj->second->my_obj = new stdClass();
$obj->second->my_obj->trash1 = "42";

$ao = new ArrayObject(array());

$obj->third->handler = $ao->getIterator();

$txt = serialize($obj);

echo $txt;

unserialize($txt);

?>
